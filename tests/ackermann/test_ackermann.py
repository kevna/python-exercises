#!/usr/bin/python2
# -*- coding: utf-8 -*-
import pytest

from ackermann.ackermann import AckermannCache

class TestAckermannCache:
    @pytest.mark.parametrize('arg_m, arg_n, expected', (
        (-1, -1, 0),
        (0, 0, 1),
        (0, 5, 6),
        (0, 10, 11),
        (1, 0, 2),
        (1, 5, 7),
        (1, 10, 12),
        (2, 0, 3),
        (2, 5, 13),
        (3, 0, 5),
        (3, 5, 253),
        (4, 0, 13),
        (4, 1, 65533),
    ))
    def test_get_ackermann(self, arg_m, arg_n, expected):
        ackermann = AckermannCache()
        actual = ackermann.get_ackermann(arg_m, arg_n)
        assert actual == expected
