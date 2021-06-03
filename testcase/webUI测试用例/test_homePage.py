#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 23:03
# @Author  : 黄权权
# @File    : test_homePage.py
# @Software: PyCharm
import allure
import pytest


@allure.epic("淘宝网站-UI自动化测试")
@allure.feature("淘宝网站首页功能测试")
class TestHomePage:
    """
    淘宝首页测试类
    """

    @pytest.mark.test
    def test1(self, init_homePage):
        self.homePage = init_homePage
        self.homePage.sliding_to_bottom()




