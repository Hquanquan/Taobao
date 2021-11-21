#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/6/6 18:01
# @Author  : 黄权权
# @File    : test_loginPage.py
# @Software: PyCharm
# @Desc    : 淘宝-登录页测试
import allure
import pytest

@allure.epic("淘宝网站-UI自动化测试")
@allure.feature("淘宝网站-登录页测试")
class TestLoginPage:
    """
    淘宝网站-登录页测试
    """

    # @pytest.mark.test
    @allure.story("登录功能测试")
    @allure.title("验证密码登录")
    def test_login_by_password(self):
        """
        验证密码登录
        :return:
        """
        pass

    # @pytest.mark.test
    @allure.story("登录功能测试")
    @allure.title("验证短信登录")
    def test_login_by_SMS(self):
        """
        验证短信登录
        :return:
        """
        pass

    # @pytest.mark.test
    @allure.story("登录功能测试")
    @allure.title("验证扫二维码登录")
    def test_login_by_SMS(self):
        """
        验证扫二维码登录
        :return:
        """
        pass


