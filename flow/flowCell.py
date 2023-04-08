#!/usr/bin/python2
# -*- coding: utf-8 -*-

class FlowCell(object):
    def __init__(self, value = None):
        if value is not None:
            self.value = value
            self.original = True
        else:
            self.value = None
            self.original = False

    def __str__(self):
        result = " "
        if self.value is not None:
            result = self.value
        return result
