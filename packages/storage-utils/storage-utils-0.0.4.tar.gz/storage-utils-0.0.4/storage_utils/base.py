#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from urllib.parse import urlparse

__all__ = ["BaseStorage"]


class BaseStorage(metaclass=ABCMeta):

    @property
    @abstractmethod
    def storage_options(self):
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def get_full_path(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_size(self, *args, **kwargs):
        pass

    @abstractmethod
    def open(self, *args, **kwargs):
        pass

    @abstractmethod
    def close(self, *args, **kwargs):
        pass

    @staticmethod
    def _parse_path(path: str):
        scheme, netloc, path, *_ = urlparse(path, scheme=None)
        return scheme, netloc, path
