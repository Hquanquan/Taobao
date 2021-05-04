#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 13:34
# @Author  : 黄权权
# @File    : conftest.py
# @Software: PyCharm
import pytest
from pylib.web_UI_lib.pageObjects.homePage import HomePage


@pytest.fixture(scope="session")
def test_test():
    homePage = HomePage()
