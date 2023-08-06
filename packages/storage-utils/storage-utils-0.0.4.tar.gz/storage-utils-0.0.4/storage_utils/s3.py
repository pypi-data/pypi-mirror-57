#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import s3fs
from .base import BaseStorage

__all__ = ["S3Storage"]
logger = logging.getLogger(__name__)


class S3Storage(BaseStorage):

    # noinspection PyUnusedLocal
    def __init__(self, fs=None, bucket=None, *args, **kwargs):
        self._storage_options = dict(
            anon=kwargs.get("anon", False), key=kwargs.get("key"), secret=kwargs.get("secret"),
            token=kwargs.get("token"), use_ssl=kwargs.get("use_ssl", True), client_kwargs=kwargs.get("client_kwargs"),
            requester_pays=kwargs.get("requester_pays", False), default_block_size=kwargs.get("default_block_size"),
            default_fill_cache=kwargs.get("default_fill_cache", True),
            default_cache_type=kwargs.get("default_cache_type", "bytes"),
            version_aware=kwargs.get("version_aware", False), config_kwargs=kwargs.get("config_kwargs"),
            s3_additional_kwargs=kwargs.get("s3_additional_kwargs"), session=kwargs.get("session"),
            username=kwargs.get("username"), password=kwargs.get("password")
        )
        if isinstance(fs, s3fs.core.S3FileSystem):
            self._fs = fs
        else:
            # noinspection PyArgumentList
            self._fs = s3fs.core.S3FileSystem(**self._storage_options)
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
        path = os.path.join(bucket.lstrip("/"), path.lstrip("/"))
        self._fs.invalidate_cache(path)
        if self._fs.isdir(path):
            path = os.path.join(path, "*")
        return f"s3://{path}"

    def get_size(self, path: str, bucket: str = None, *args, **kwargs):
        scheme, netloc, path = self._parse_path(path)
        if scheme:
            path = os.path.join(netloc, path.lstrip("/"))
        else:
            if bucket is None:
                bucket = self.bucket
            path = os.path.join(bucket.lstrip("/"), path.lstrip("/"))
        if path.endswith("/*"):
            path = path.rstrip("/*")
        self._fs.invalidate_cache(path)
        return self._fs.disk_usage(path)

    def open(self, path: str, bucket: str = None, mode: str = "rb",
             block_size: int = None, cache_options=None, *args, **kwargs):
        scheme, netloc, path = self._parse_path(path)
        if scheme:
            path = os.path.join(netloc, path.lstrip("/"))
        else:
            if bucket is None:
                bucket = self.bucket
            path = os.path.join(bucket.lstrip("/"), path.lstrip("/"))
        self._fs.invalidate_cache(path)
        if not self._fs.isfile(path):
            raise IOError(f"\"{path}\" is not a file.")
        return self._fs.open(path, mode=mode,
                             block_size=block_size, cache_options=cache_options)

    def close(self, f=None, *args, **kwargs):
        if hasattr(f, "close"):
            closed = False
            if hasattr(f, "closed"):
                closed = f.closed
            if not closed:
                f.close()
