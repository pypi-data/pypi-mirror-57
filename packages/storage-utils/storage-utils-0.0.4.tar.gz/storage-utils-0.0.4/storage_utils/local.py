#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import platform
from .base import BaseStorage

__all__ = ["LocalStorage"]
logger = logging.getLogger(__name__)

if platform.system() == "Windows":
    msg_err = "this package does not work on Windows"
    logger.critical(msg_err)
    raise ImportError(msg_err)


class LocalStorage(BaseStorage):

    # noinspection PyUnusedLocal
    def __init__(self, fs=None, bucket=None, *args, **kwargs):
        self._storage_options = None
        self.bucket = bucket
        if self.bucket is None:
            self.bucket = ""

    @property
    def storage_options(self):
        return self._storage_options

    def connect(self):
        pass

    def disconnect(self):
        pass

    def get_full_path(self, path: str, bucket: str = None, *args, **kwargs):
        scheme, *_ = self._parse_path(path)
        if scheme:
            return path
        if bucket is None:
            bucket = self.bucket
        path = os.path.join("/", bucket, path.lstrip("/"))
        if os.path.isdir(path):
            path = os.path.join(path, "*")
        return f"file://{path}"

    def get_size(self, path: str, bucket: str = None, *args, **kwargs):
        scheme, netloc, path = self._parse_path(path)
        if scheme:
            path = os.path.join("/", netloc, path.lstrip("/"))
        else:
            if bucket is None:
                bucket = self.bucket
            path = os.path.join("/", bucket, path.lstrip("/"))
        if path.endswith("/*"):
            path = path.rstrip("/*")
        isdir = os.path.isdir(path)
        if isdir:
            size = 0
            for dirpath, dirnames, filenames in os.walk(path):
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    if not os.path.islink(filepath):
                        size += os.path.getsize(filepath)
        else:
            size = os.path.getsize(path)
        return size

    def open(self, path: str, bucket: str = None, mode: str = "rb",
             buffering=None, encoding="utf-8", errors=None, newline=None, closefd=True, *args, **kwargs):
        scheme, netloc, path = self._parse_path(path)
        if scheme:
            path = os.path.join("/", netloc, path.lstrip("/"))
        else:
            if bucket is None:
                bucket = self.bucket
            path = os.path.join("/", bucket, path.lstrip("/"))
        if os.path.isdir(path):
            raise IOError(f"\"{path}\" is not a file.")
        buffering_ = {} if buffering is None else {"buffering": buffering}
        # noinspection PyArgumentList
        return open(path, mode=mode, encoding=encoding,
                    errors=errors, newline=newline, closefd=closefd, **buffering_)

    def close(self, f=None, *args, **kwargs):
        if hasattr(f, "close"):
            closed = False
            if hasattr(f, "closed"):
                closed = f.closed
            if not closed:
                f.close()
