#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import pyarrow
from .base import BaseStorage

__all__ = ["HDFSStorage"]
logger = logging.getLogger(__name__)

if not os.getenv("HADOOP_CONF_DIR"):
    logger.warning("\"HADOOP_CONF_DIR\" has not been set.")


class HDFSStorage(BaseStorage):

    # noinspection PyUnusedLocal
    def __init__(self, fs=None, bucket=None, *args, **kwargs):
        self._storage_options = dict(
            host=kwargs.get("host", "default"),
            port=kwargs.get("port", 0),
            user=kwargs.get("user"),
            kerb_ticket=kwargs.get("kerb_ticket"),
            driver=kwargs.get("driver", "libhdfs"),
            extra_conf=kwargs.get("extra_conf")
        )
        if isinstance(fs, pyarrow.hdfs.HadoopFileSystem):
            self._fs = fs
        else:
            # noinspection PyArgumentList
            self._fs = pyarrow.hdfs.connect(**self._storage_options)
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
        if self._fs.isdir(path):
            path = os.path.join(path, "*")
        return f"hdfs://{path}"

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
        return self._fs.disk_usage(path)

    def open(self, path: str, bucket: str = None, mode: str = "rb",
             buffer_size=None, replication=None, default_block_size=None, *args, **kwargs):
        scheme, netloc, path = self._parse_path(path)
        if scheme:
            path = os.path.join("/", netloc, path.lstrip("/"))
        else:
            if bucket is None:
                bucket = self.bucket
            path = os.path.join("/", bucket, path.lstrip("/"))
        if not self._fs.isfile(path):
            raise IOError(f"\"{path}\" is not a file.")
        return self._fs.open(path, mode=mode,
                             buffer_size=buffer_size, replication=replication, default_block_size=default_block_size)

    def close(self, f=None, *args, **kwargs):
        if hasattr(f, "close"):
            closed = False
            if hasattr(f, "closed"):
                closed = f.closed
            if not closed:
                f.close()
