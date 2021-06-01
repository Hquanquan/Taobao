#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 13:13
# @Author  : 黄权权
# @File    : test_commonPage.py
# @Software: PyCharm
import allure
import pytest


@allure.epic("淘宝网站-UI自动化测试")
@allure.feature("淘宝网站-顶部导航栏模块功能测试")
class TestCommonPage:
    """
    淘宝网站顶部导航栏测试类
    """

    # @pytest.mark.test
    @allure.story("顶部导航栏左侧按钮功能测试")
    @allure.title("验证鼠标悬停【中国大陆】效果")
    def test_move_to_nav_left_location(self, init_commonPage):
        """
        鼠标悬停【中国大陆】,弹出13个地区名称列表
        :param init_commomPage:
        :return:
        """
        self.commonPage = init_commonPage
        # 鼠标悬停【中国大陆】
        self.commonPage.move_to_nav_left_location()
        # 获取悬停后显示的那一组地区名称
        locationNames = self.commonPage.get_nav_left_locations_text()
        # 预期地区名称
        expect_locationNames = ['全球', '中国大陆', '中国香港', '中国台湾', '中国澳门', '韩国', '马来西亚', '澳大利亚', '新加坡', '新西兰', '加拿大', '美国',
                                '日本']
        assert locationNames == expect_locationNames

    # @pytest.mark.test
    @allure.story("顶部导航栏左侧按钮功能测试")
    @allure.title("验证未登录时，显示【亲，请登录】按钮")
    def test_isDisplay_nav_left_Login(self, init_commonPage):
        """
        验证未登录时，显示【亲，请登录】按钮
        :return:
        """
        self.commonPage = init_commonPage
        result = self.commonPage.isDisplay_nav_left_Login()
        assert result == True

    @pytest.fixture()
    def after_test_click_nav_left_Login_btn(self, init_commonPage, init_loginPage):
        """
        验证未登录时，点击【亲，请登录】按钮，跳转到登录页面,
        后置处理，返回上一页
        :param init_commonPage:
        :param init_loginPage:
        """
        self.commonPage = init_commonPage
        self.loginPage = init_loginPage
        yield
        self.loginPage.back_browser()

    @allure.story("顶部导航栏左侧按钮功能测试")
    @allure.title("验证未登录时，点击【亲，请登录】按钮，跳转到登录页面")
    def test_click_nav_left_Login_btn(self, after_test_click_nav_left_Login_btn):
        """
        验证未登录时，点击【亲，请登录】按钮，跳转到登录页面
        :param after_test_click_nav_left_Login_btn:
        :return:
        """
        # 点击【亲，请登录】
        self.commonPage.click_nav_left_Login_btn()
        # 页面跳转到了LoginPage登录页面
        text = self.loginPage.get_login_text()
        assert text == "密码登录"

    @pytest.fixture()
    def after_test_click_nav_left_register_btn(self, init_commonPage, init_registerPage):
        """
        验证未登录时，点击【免费注册】按钮，跳转到注册页面,后置处理，返回上一页
        :param init_commonPage:
        :param init_registerPage:
        :return:
        """
        self.commonPage = init_commonPage
        self.registerPage = init_registerPage
        yield
        self.registerPage.back_browser()

    # @pytest.mark.test
    @allure.story("顶部导航栏左侧按钮功能测试")
    @allure.title("验证未登录时，点击【免费注册】按钮，跳转到注册页面")
    def test_click_nav_left_register_btn(self, after_test_click_nav_left_register_btn):
        """
        验证未登录时，点击【免费注册】按钮，跳转到注册页面
        :return:
        """
        self.commonPage.click_nav_left_register_btn()
        title = self.registerPage.get_url_title()
        assert title == "注册"

    @pytest.fixture()
    def after_test_click_nav_left_taobao_btn(self, init_commonPage, init_downloadPage):
        """

        :param init_commonPage:
        :param init_downloadPage:
        """
        self.commonPage = init_commonPage
        self.downloadPage = init_downloadPage
        yield
        self.downloadPage.back_browser()

    # @pytest.mark.test
    @allure.story("顶部导航栏左侧按钮功能测试")
    @allure.title("验证未登录时，点击【手机淘宝】按钮，跳转到PC下载页")
    def test_click_nav_left_taobao_btn(self, after_test_click_nav_left_taobao_btn):
        """
        验证未登录时，点击【手机淘宝】按钮，跳转到PC下载页
        :param after_test_click_nav_left_taobao_btn:
        :return:
        """
        # 点击【手机淘宝】按钮
        self.commonPage.click_nav_left_taobao_btn()
        # 页面跳转到PC页
        # 获取当前页面标题
        title = self.downloadPage.get_url_title()
        assert title == "PC下载页"

    @pytest.fixture()
    def after_test_click_nav_right_mytaobao_btn(self, init_commonPage, init_loginPage):
        """
        验证未登录时，点击【我的淘宝】按钮，跳转到登录页,后置处理，返回上一页
        :param init_commonPage:
        :param init_loginPage:
        """
        self.commonPage = init_commonPage
        self.loginPage = init_loginPage
        yield
        self.loginPage.back_browser()

    # @pytest.mark.test
    @allure.story("顶部导航栏左侧按钮功能测试")
    @allure.title("验证未登录时，点击【我的淘宝】按钮，跳转到登录页")
    def test_click_nav_right_mytaobao_btn(self, after_test_click_nav_right_mytaobao_btn):
        """
        验证未登录时，点击【我的淘宝】按钮，跳转到登录页
        :param after_test_click_nav_right_mytaobao_btn:
        :return:
        """
        # 点击【我的淘宝】
        self.commonPage.click_nav_right_mytaobao_btn()
        # 页面跳转到了LoginPage登录页面
        # 获取登录页面特有文案
        text = self.loginPage.get_login_text()
        assert text == "密码登录"

    @pytest.fixture()
    def after_test_click_nav_right_cart_btn(self, init_commonPage, init_loginPage):
        """
        验证未登录时，点击【购物车】按钮，跳转到登录页,后置处理，返回上一页
        :param init_commonPage:
        :param init_loginPage:
        """
        self.commonPage = init_commonPage
        self.loginPage = init_loginPage
        yield
        self.loginPage.back_browser()

    @pytest.mark.test
    @allure.story("顶部导航栏左侧按钮功能测试")
    @allure.title("验证未登录时，点击【购物车】按钮，跳转到登录页")
    def test_click_nav_right_cart_btn(self, after_test_click_nav_right_cart_btn):
        """
        验证未登录时，点击【购物车】按钮，跳转到登录页
        :param after_test_click_nav_right_cart_btn:
        :return:
        """
        # 点击购物车
        self.commonPage.click_nav_right_cart_btn()
        # 页面跳转到登录页面
        text = self.loginPage.get_login_text()
        assert text == "密码登录"
