#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import os
from storage_utils import LocalStorage


class TestLocalStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.this_dir = os.path.abspath(os.path.dirname(__file__))
        cls.storage = LocalStorage(bucket=cls.this_dir)
        cls.file = os.path.basename(__file__)

    def test_storage_options(self):
        self.assertIsNone(self.storage.storage_options)

    def test_full_path(self):
        full_path_ = "file://" + os.path.join(self.this_dir, self.file)
        full_path = self.storage.get_full_path(self.file)
        self.assertEqual(full_path, full_path_)

    def test_size(self):
        size = self.storage.get_size(self.file)
        self.assertIsInstance(size, int)
        self.assertNotEqual(size, 0)

    def test_open(self):
        f = self.storage.open(self.file, mode="rb")
        first_line = f.readline()
        self.storage.close(f)
        first_line_ = b"#!/usr/bin/env python3\n"
        self.assertEqual(first_line, first_line_)


if __name__ == "__main__":
    unittest.main()
