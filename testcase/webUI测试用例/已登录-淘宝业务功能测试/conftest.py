#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/6/6 18:41
# @Author  : 黄权权
# @File    : conftest.py
# @Software: PyCharm
# @Desc    : 描述文件内容
import pytest

from pylib.web_UI_lib.pageObjects.homePage import HomePage
from pylib.web_UI_lib.pageObjects.loginPage import LoginPage

@pytest.fixture(scope="session")
def user_login():
    """
    用户登录
    :return:
    """
    homePage = HomePage()
    loginPage = LoginPage()
    # 点击，请登录
    homePage.click_nav_left_Login_btn()
    # 页面跳转到登录页面
    # 点击二维码，进行扫码登录
    loginPage.click_QR_Code()
    input("请扫码完成后输入：1，并按下 enter")

    yield homePage
