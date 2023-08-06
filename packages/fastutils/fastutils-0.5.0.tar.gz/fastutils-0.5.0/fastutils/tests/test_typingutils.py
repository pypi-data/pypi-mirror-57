# -*- coding: utf-8 -*-
import unittest
import os
import binascii
import base64
import codecs
import typing
from fastutils.typingutils import smart_cast

class TestStrUtils(unittest.TestCase):

    def test01(self):
        assert smart_cast(int, "12") == 12
        assert smart_cast(float, "12.34") == 12.34
        assert smart_cast(bool, "true") == True
        assert smart_cast(bytes, "6869") == b"hi"
        assert smart_cast(list, "1,2,3") == ["1", "2", "3"]
        assert smart_cast(list, "[1, 2, 3]") == [1, 2, 3]
        assert smart_cast(dict, """{"a": "a", "b": "b"}""") == {"a": "a", "b": "b"}
        assert smart_cast(typing.Mapping, """{"a": "a", "b": "b"}""") == {"a": "a", "b": "b"}
