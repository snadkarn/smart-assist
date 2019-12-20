# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 17:12:01 2019

@author: shrey
"""

from win32api import GetSystemMetrics
print("Width =", GetSystemMetrics(0))
print("Height =", GetSystemMetrics(1))