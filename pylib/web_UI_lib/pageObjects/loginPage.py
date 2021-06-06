#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 11:15
# @Author  : 黄权权
# @File    : loginPage.py
# @Software: PyCharm
# @Desc    : 淘宝网站登录页面
import allure

from pylib.web_UI_lib.pageObjects.basePage import BasePage


class LoginPage(BasePage):
    """
    淘宝网站登录页面,
    1、页面元素
    2、相关页面元素的方法
    """

    def __init__(self):
        # 继承父类的__init__()构造方法
        # super().__init__()
        super(LoginPage, self).__init__()

        # 密码登录
        self.login_text = ['xpath', '//*[@id="login"]/div[2]/div/div[1]/a[1]']
        # 会员名/邮箱/手机号 输入框
        self.userName_input = ["id", "#fm-login-id"]
        # 登录密码 输入框
        self.password_input = ["id", "#fm-login-password"]
        # 短信登录
        self.SMS_login = ['xpath', '//*[@id="login"]/div[2]/div/div[1]/a[2]']
        # 手机号输入框
        self.phone_input = ["id", "#fm-sms-login-id"]
        # 短信验证码输入框
        self.smsCode_input = ["id", "#fm-smscode"]
        # 获取验证码 按钮
        self.Code_btn = ["xpath", '//*[@id="login-form"]/div[2]/div[3]/a']
        # 右上角一半二维码
        self.QR_Code = ["css selector", "#login > div.corner-icon-view.view-type-qrcode > i"]
        # 登录按钮
        self.login_btn = ["css selector", "#login-form > div.fm-btn > button"]

    def get_login_text(self):
        """
        获取登录页面中，密码登录文案
        :return:
        """
        return self.get_element_text(self.login_text)

    @allure.step("step:点击二维码，进行扫描登录")
    def click_QR_Code(self):
        """
        点击二维码，进行扫描登录
        :return:
        """
        self.click(self.QR_Code)
