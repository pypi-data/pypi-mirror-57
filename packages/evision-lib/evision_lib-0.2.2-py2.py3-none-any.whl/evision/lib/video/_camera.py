#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2019 eVision.ai Inc. All Rights Reserved.
#
# @author: Chen Shijiang(chenshijiang@evision.ai)
# @date: 2019-10-12 15:56
# @version: 1.0
#
import queue
import time
from threading import Thread

import cv2
import numpy as np

from evision.lib.log import LogHandlers, logutil
from evision.lib.video import BaseImageProvider
from evision.lib.video.base import ImageSourceType, ImageSourceUtil

logger = logutil.get_logger(LogHandlers.DEFAULT)


class VideoCaptureSource(BaseImageProvider):
    """VideoCapture类型的视频源封装"""
    __camera: cv2.VideoCapture

    def read_frame(self):
        """从视频源直接获取图像帧"""
        try:
            with self._lock:
                ret, camera_frame = self.__camera.read()
            if not ret or np.all(camera_frame == 0):
                self.accumulate_failure_count()
                self.try_restore(self._MAX_FAIL_TIMES, self.reload_source)
                time.sleep(self.frame_interval)
                return None
            self.reset_failure_count()
            return camera_frame
        except Exception as e:
            logger.exception('Failed reading from camera={}: {}',
                             self.__camera, e)
        return None

    def work(self):
        camera_frame = self.read_frame()
        if camera_frame is None:
            logger.info('Read no frame, waiting for {:.3f}s', self.frame_interval)
            time.sleep(self.frame_interval)
            return

        try:
            if not self._frame_queue.empty():
                self._frame_queue.get_nowait()
        except queue.Empty:
            pass
        try:
            self._frame_queue.put_nowait(camera_frame)
        except queue.Full:
            pass

    def init(self):
        """创建VideoCapture对象"""
        __camera = self.validate_camera_source(self.source, self.type,
                                               release=False)

        if __camera is None or not __camera.isOpened():
            raise Exception('摄像头无法连接，请检查')

        camera_frame_width = __camera.get(cv2.CAP_PROP_FRAME_WIDTH)
        camera_frame_height = __camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
        camera_fps = __camera.get(cv2.CAP_PROP_FPS)
        logger.info('Camera connected, width={}, height={}, frame_rate={}',
                    camera_frame_width, camera_frame_height, camera_fps)
        self.original_frame_width = camera_frame_width
        self.original_frame_height = camera_frame_height
        self.original_fps = camera_fps

        # set properties according to camera type
        if self.type and ImageSourceType.USB_CAMERA.equals(self.type):
            __camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)
            __camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)
            __camera.set(cv2.CAP_PROP_FPS, self.fps)
            self.zoom_ratio = 1
        else:
            if self.frame_width:
                self.zoom_ratio = float(self.frame_width) / camera_frame_width
                self.frame_height = int(camera_frame_height * self.zoom_ratio)
            elif self.frame_height:
                self.zoom_ratio = float(self.frame_height) / camera_frame_height
                self.frame_width = int(camera_frame_width * self.zoom_ratio)
            else:
                self.zoom_ratio = 1
                self.frame_width = camera_frame_width
                self.frame_height = camera_frame_height

        self.__camera = __camera

    def _update_zoom_ratio(self):
        if self.__camera and self.type and ImageSourceType.USB_CAMERA.equals(self.type):
            self.__camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)
            self.__camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)
            self.__camera.set(cv2.CAP_PROP_FPS, self.fps)
            self.zoom_ratio = 1
        else:
            super()._update_zoom_ratio()

    @staticmethod
    def validate_camera_source(camera_source,
                               camera_type=ImageSourceType.IP_CAMERA,
                               release=True):
        """验证VideoCapture对象是否有效"""
        camera_source, camera_type = ImageSourceUtil.parse_video_source(
            camera_source, camera_type)
        __camera = cv2.VideoCapture(camera_source)
        if not __camera.isOpened():
            logger.warning('Failed connecting to camera=[{}], type={}',
                           camera_source, camera_type)
            return None

        ret, frame = __camera.read()

        if not ret:
            logger.warning('Camera[{}, type={}] opened but failed getting frame',
                           camera_source, camera_type)
            return None

        if release:
            __camera.release()
            return frame

        return __camera

    def reload_source(self):
        self.reset_failure_count()
        with self._lock:
            try:
                source_ = cv2.VideoCapture(self.source)
                if source_ is None or not source_.isOpened():
                    raise Exception('Failed initialized video source={}'.format(
                        self.source))
                self.__camera.release()
                self.__camera = source_
            except Exception as e:
                logger.error('[{}] Failed reloading camera={}: {}',
                             self.id, self.source, e)
        logger.info('Reload video source={}', self.source)

    def stop_reading(self, release=True):
        self._keep_running = False
        if release and self.__camera:
            self.__camera.release()
            del self.__camera


class VideoCapturePreview(Thread):
    """视频源预览,需要图形界面支持"""

    def __init__(self, camera):
        Thread.__init__(self)
        self.camera = camera

    def run(self):
        if self.camera.zone is not None:
            text_org = (self.camera.zone.start_x + 4, self.camera.zone.end_y - 4)
        else:
            text_org = None
        while True:
            frame = self.camera.get()
            if frame is None:
                continue
            if text_org:
                cv2.putText(frame, 'Detection Zone',
                            org=text_org,
                            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                            fontScale=0.5, color=(0, 255, 0), lineType=2)
                cv2.rectangle(frame,
                              self.camera.zone.start_point,
                              self.camera.zone.end_point,
                              (0, 255, 0), 2)
            cv2.imshow(self.camera.alias, frame)

            if cv2.waitKey(200) & 0xFF == ord('q'):
                cv2.destroyWindow(self.camera.alias)
                break


if __name__ == '__main__':
    video_file = '~/Downloads/test.avi'
    import os

    video_source = VideoCaptureSource(source=os.path.expanduser(video_file),
                                      type=ImageSourceType.VIDEO_FILE, fps=5)
    video_source.daemon = True
    video_source.start()

    preview = VideoCapturePreview(video_source)
    preview.run()

    video_source.stop_reading()
