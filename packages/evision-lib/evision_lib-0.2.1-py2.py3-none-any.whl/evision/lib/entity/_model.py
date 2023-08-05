# -*- coding: utf-8 -*-
#
# Copyright 2019 eVision.ai Inc. All Rights Reserved.
#
# @author: Chen Shijiang(chenshijiang@evision.ai)
# @date: 2019-11-29 18:23
# @version: 1.0
#

import collections
import time
from typing import Union

import cv2
import numpy as np
from pydantic import BaseModel, root_validator, validator

__all__ = [
    'Size', 'Shape',
    'Vertex', 'Vector',
    'Zone',
    'ImageFrame',
    'Detection'
]


class Shape(BaseModel):
    width: int
    height: int

    @classmethod
    def parse(cls, value):
        if value is None:
            return None
        elif isinstance(value, Shape):
            return value
        elif isinstance(value, collections.abc.Sequence):
            return Shape(width=value[0], height=value[1])
        return None

    @validator('width', 'height')
    def ensure_positive(cls, v):
        assert v > 0, 'Value should be positive'
        return v

    def to_list(self):
        return [self.width, self.height]

    def to_tuple(self):
        return self.width, self.height

    def __str__(self):
        return '({}, {})'.format(self.width, self.height)


Size = Shape


class Vertex(BaseModel):
    x: Union[int, float]
    y: Union[int, float]

    def to_list(self):
        return [self.x, self.y]

    def to_tuple(self):
        return self.x, self.y

    def times(self, times):
        return self.__class__(x=self.x * times, y=self.y * times)

    @classmethod
    def _parse(cls, value):
        if value is None:
            return None
        elif isinstance(value, Vertex):
            return value
        elif isinstance(value, collections.abc.Sequence):
            return Vertex(x=value[0], y=value[1])
        return None

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __eq__(self, other):
        other = Vertex._parse(other)
        if not other:
            return False
        return self.x == other.x and self.y == other.y

    def __len__(self):
        """collections.Sized"""
        return 0 if self.x is None or self.y is None else 2

    def __iter__(self):
        """collections.Iterable"""
        return iter(self.to_list())

    def __add__(self, other):
        other = Vertex._parse(other)
        if not other:
            raise ValueError(f'Invalid vertex: {other}')
        return Vertex(x=self.x + other.x, y=self.y + other.y)

    def __sub__(self, other):
        other = Vertex._parse(other)
        if not other:
            raise ValueError(f'Invalid vertex: {other}')
        return Vertex(x=self.x - other.x, y=self.y - other.y)

    def __mul__(self, other):
        other = Vertex._parse(other)
        if not other:
            raise ValueError(f'Invalid vertex: {other}')
        return Vertex(x=self.x * other.x, y=self.y * other.y)


Vector = Vertex


class Zone(BaseModel):
    # __aspect_ratio = 1.25  # 5 / 4
    __aspect_ratio: int = 1  # 1 / 1
    __expand_ratio: int = 0.33
    start_x: int
    start_y: int
    width: int = None
    height: int = None
    end_x: int = None
    end_y: int = None
    bias_x: int = 0
    bias_y: int = 0

    class Config:
        arbitrary_types_allowed = True
        # keep_untouched = (property,)

    @root_validator(pre=True)
    def ensure_arguments(cls, values):
        start_x, start_y = values['start_x'], values['start_y']

        if 'width' in values and 'height' in values:
            width, height = values['width'], values['height']
            values['end_x'] = start_x + width
            values['end_y'] = start_y + height
        elif 'end_x' in values and 'end_y' in values:
            end_x, end_y = values['end_x'], values['end_y']
            values['width'] = end_x - start_x
            values['height'] = end_y - start_y
        else:
            raise ValueError('Argument pair (width, height) or (end_x, end_y) '
                             'should be fully set')
        return values

    @validator('start_x', 'start_y', allow_reuse=True)
    def ensure_non_negative(cls, v):
        assert v >= 0, 'should be non-negative'
        return v

    @validator('end_x', 'end_y', 'width', 'height', allow_reuse=True)
    def ensure_positive(cls, v):
        assert v > 0, 'should be non-negative'
        return v

    @property
    def area(self):
        return self.width * self.height

    @property
    def start_point(self):
        return Vertex(x=self.start_x, y=self.start_y)

    @property
    def end_point(self):
        return Vertex(x=self.end_x, y=self.end_y)

    top_left = start_point
    bottom_right = end_point

    @property
    def top_right(self):
        return Vertex(x=self.end_x, y=self.start_y)

    @property
    def bottom_left(self):
        return Vertex(x=self.start_x, y=self.end_y)

    @property
    def center(self):
        return Vertex(x=self.start_x + int(self.width / 2),
                      y=self.start_y + int(self.height / 2))

    @property
    def bias(self):
        return Vector(x=self.bias_x, y=self.bias_y)

    @bias.setter
    def bias(self, value):
        assert isinstance(value, collections.abc.Sized) and len(value) == 2
        assert isinstance(value, collections.abc.Iterable)
        self.bias_x, self.bias_y = value

    @property
    def shape(self):
        return self.width, self.height

    def validate_shape(self, width, height):
        invalid_x = self.start_x < 0 and self.end_x > width
        invalid_y = self.start_y < 0 and self.end_y > height
        if invalid_x or invalid_y:
            raise ValueError(
                'Invalid zone config, start={}, size={}, frame size=[{}, {}]'.format(
                    self.start_point, self.shape, width, height))

    def move(self, x, y):
        """移动区域"""
        self.start_x += x
        self.start_y += y
        self.end_x = self.start_x + self.width
        self.end_y = self.start_y + self.height

    @property
    def description(self):
        return {
            'x': self.start_x,
            'y': self.start_y,
            'w': self.width,
            'h': self.height,
            'x2': self.end_x,
            'y2': self.end_y,
            'bias_x': self.bias_x,
            'bias_y': self.bias_y
        }

    def get_zone(self, origin, bias_x=0, bias_y=0):
        """Get Cropped zone

        :param origin: full image frame
        :param bias_x: 裁剪图像区域时的横向偏移
        :param bias_y: 裁剪图像区域时的纵向偏移
        :return: cropped zone
        """
        if bias_x != 0 or bias_y != 0:
            self.move(bias_x, bias_y)
        result = origin[self.start_y:self.end_y, self.start_x:self.end_x]
        if bias_x != 0 or bias_y != 0:
            self.move(-bias_x, -bias_y)
        return result

    def expanded_zone(self, origin, bias_x=0, bias_y=0):
        """Get expanded zone with specific aspect ratio

        Face zone detected(Bounding box) with MTCNN is quite tight for viewing,
        we expand the detection zone out of displaying necessity.

        :param origin: 原始图像
        :param bias_x: 横轴方向偏移
        :param bias_y: 纵轴方向偏移
        :return: expanded zone
        """
        frame_height, frame_width, _ = origin.shape
        start_point, end_point = self.expanded_anchor(frame_width, frame_height,
                                                      bias_x, bias_y)
        result = origin[start_point.y:end_point.y, start_point.x:end_point.x]
        return result

    def expanded_anchor(self, frame_width, frame_height,
                        bias_x=0, bias_y=0,
                        aspect_ratio=None, max_expand_ratio=None) -> (Vertex, Vertex):
        """指定缩放比例获取图像扩张之后的关键点

        :param frame_width: 宽度限制
        :param frame_height: 高度限制
        :param bias_x: 包围盒偏移
        :param bias_y: 包围盒偏移
        :param aspect_ratio: 高宽比限制
        :param max_expand_ratio: 扩张比例限制
        :return 可扩展区域左上角点坐标和右下角点坐标
        """
        aspect_ratio = aspect_ratio if aspect_ratio else self.__aspect_ratio
        max_expand_ratio = max_expand_ratio if max_expand_ratio else self.__expand_ratio

        if bias_x != 0 or bias_y != 0:
            self.move(bias_x, bias_y)
        cur_aspect_ratio = self.height / self.width

        expand_ratio = min(frame_width / max(self.height / aspect_ratio, self.width),
                           frame_height / max(self.width * aspect_ratio, self.height))
        expand_ratio = min((expand_ratio - 1) / 2, max_expand_ratio)

        # 如果检测区域比较“矮胖”，先在横轴方向进行扩充
        if cur_aspect_ratio < aspect_ratio:
            resize_width = int((2 * expand_ratio + 1) * self.width)
            padding_left = int(expand_ratio * self.width)
            start_x = max(min(self.start_x - padding_left, frame_width - resize_width), 0)

            resize_height = int(resize_width * aspect_ratio)
            padding_top = int((resize_height - self.height) / 2)
            start_y = max(min(self.start_y - padding_top, frame_height - resize_height), 0)
        # 如果检测区域比较“高瘦”，先在纵轴方向进行扩充
        else:
            resize_height = int((2 * expand_ratio + 1) * self.height)
            padding_top = int(expand_ratio * self.height)
            start_y = max(min(self.start_y - padding_top, frame_height - resize_height), 0)

            resize_width = int(resize_height / aspect_ratio)
            padding_left = int((resize_width - self.width) / 2)
            start_x = max(min(self.start_x - padding_left, frame_width - resize_width), 0)

        end_x = start_x + resize_width
        end_y = start_y + resize_height
        if bias_x != 0 or bias_y != 0:
            self.move(-bias_x, -bias_y)
        return Vertex(x=start_x, y=start_y), Vertex(x=end_x, y=end_y)

    def __str__(self):
        return '[{}, {}], shape={}'.format(
            self.start_point, self.end_point, self.shape)

    def __repr__(self):
        return str(self)


class ImageFrame(object):
    """图像帧

    可以指定检测区域
    """

    def __init__(self, source_id, frame_id, frame=None,
                 zoom_ratio=1, zone: Zone = None):
        """缩放比例优先于检测区域，即检测区域是在缩放后的图像上选取"""
        self.source_id = source_id
        self.frame_id = frame_id
        self.frame = frame

        self.zoom_ratio = zoom_ratio
        self.zone = zone

        self.timestamp = int(time.time())
        self.extras = {}

    @property
    def is_zoomed(self):
        return self.zoom_ratio > 0 and self.zoom_ratio != 1

    @property
    def size(self):
        h, w, _ = self.frame.shape
        return w, h

    @property
    def bias(self):
        if not self.zone:
            return 0, 0
        else:
            return self.zone.start_x, self.zone.start_y

    @property
    def resized_size(self):
        """缩放后的图像尺寸：（宽，高）"""
        if not self.is_zoomed:
            return self.size
        else:
            return tuple(int(_ * self.zoom_ratio) for _ in self.size)

    @property
    def resized_frame(self):
        """获取缩放后的图像帧"""
        if not self.is_zoomed:
            return self.frame
        else:
            return cv2.resize(self.frame, self.resized_size,
                              interpolation=cv2.INTER_CUBIC)

    @property
    def detection_zone(self):
        """检测区域"""
        return self.zone.get_zone(self.resized_frame) if self.zone else self.resized_frame

    @property
    def detection_zone_size(self):
        """检测区域尺寸"""
        h, w, _ = self.detection_zone.shape
        return w, h

    def extract_zone(self, zone: Zone):
        if not zone:
            return None
        bias_x, bias_y = self.bias
        return zone.get_zone(self.resized_frame, bias_x, bias_y)

    def extract_expanded_zone(self, zone: Zone):
        if not zone:
            return None
        bias_x, bias_y = self.bias
        return zone.expanded_zone(self.resized_frame, bias_x, bias_y)

    def __str__(self):
        return '{}-{}'.format(self.source_id, self.frame_id)

    def __repr__(self):
        return '{}: {}'.format(str(self), str(self.zone))


class Detection(Zone):
    """一个检测结果"""
    rotation: float
    feature: np.ndarray
    start_time: float
    end_time: float = None

    class Config:
        arbitrary_types_allowed = True

    @validator('end_time', allow_reuse=True)
    def set_end_time(cls, v):
        return v or time.perf_counter()

    @validator('feature', allow_reuse=True)
    def set_feature(cls, v):
        return np.array(v)

    @property
    def elapsed(self):
        """检测耗费时间，单位为ms"""
        if self.start_time is None:
            return -1
        return int(1000.0 * (self.end_time - self.start_time))

    def __repr__(self):
        return str(self)
