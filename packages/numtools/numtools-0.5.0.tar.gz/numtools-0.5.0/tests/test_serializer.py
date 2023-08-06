#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `numtools.serializer` package."""

from collections import UserDict

import numpy as np
import pytest

from numtools import serializer
from numtools.serializer import Serializer, set_loglevel


class MyData(UserDict, Serializer):
    def __init__(self):
        super().__init__()
        self.a = 5

    def __repr__(self):
        return 'MyData'


class MyStruc(Serializer):
    def __init__(self):
        self.data = {'a': True, 'mydata': MyData(), 'processed': set()}

    def __repr__(self):
        return 'MyStruc'


def test_dic2_msgpack():
    set_loglevel('info')

    mystruc = MyStruc()
    mystruc.data['mydata'][5] = 'hello'
    mystruc.data['mydata'][6] = 'world!'
    mystruc.data['mydata']['6'] = '... and the rest of the universe'
    mystruc.data['mydata']['s'] = set((1, 2, 3))

    md1 = MyStruc()
    md1.from_msgpack(mystruc.to_msgpack())
    assert md1.data['mydata'][5] == 'hello'
    assert md1.data['mydata'][6] == 'world!'
    assert md1.data['mydata']['6'] == '... and the rest of the universe'
    assert md1.data['mydata']['s'] == set((1, 2, 3))


def test_dic2_json():
    set_loglevel('info')

    mystruc = MyStruc()
    mystruc.data['mydata'][5] = 'hello'
    mystruc.data['mydata'][6] = 'world!'
    mystruc.data['mydata']['6'] = '... and the rest of the universe'
    mystruc.data['mydata']['s'] = set((1, 2, 3))

    md1 = MyStruc()
    md1.from_json(mystruc.to_json())
    assert md1.data['mydata'][5] == 'hello'
    # key#6 has been overwritten silently by JSON :-/
    assert md1.data['mydata'][6] == '... and the rest of the universe'
    assert md1.data['mydata']['s'] == set((1, 2, 3))

    # do not convert integer keys:

    serializer.FIX_JSON_INTAGER_KEYS = False
    md1 = MyStruc()
    md1.from_json(mystruc.to_json())
    assert md1.data['mydata']['5'] == 'hello'
    # key#6 has been overwritten silently by JSON :-/
    assert md1.data['mydata']['6'] == '... and the rest of the universe'
    assert md1.data['mydata']['s'] == set((1, 2, 3))
