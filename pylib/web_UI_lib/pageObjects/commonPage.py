#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 23:31
# @Author  : 黄权权
# @File    : commonPage.py
# @Software: PyCharm
# @Desc    : 淘宝-顶部导航栏
import allure

from pylib.web_UI_lib.pageObjects.basePage import BasePage


class CommonPage(BasePage):
    """
    淘宝-顶部导航栏
    """

    def __init__(self):
        # 继承父类的__init__()构造方法
        super().__init__()

        # 中国大陆
        self.nav_left_location = ["css selector", "#J_SiteNavBd .site-nav-menu-hd .site-nav-region"]
        # 中国大陆  一组元素
        self.nav_left_locations = ["xpath", '//*[@id="J_SiteNavRegionList"]/li']
        # 亲，请登录
        self.nav_left_Login = ["xpath", '//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]']
        # 点击免费注册
        self.nav_left_register = ['xpath', '//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[2]']
        # 用户名称(已登录时)
        self.nav_left_user = ['xpath', '//*[@id="J_SiteNavLogin"]/div[1]/div[2]']
        # 手机逛淘宝
        self.nav_left_taobao = ['id', 'J_SiteNavMobile']
        # 我的淘宝
        self.nav_right_mytaobao = ['id', 'J_SiteNavMytaobao']
        # 购物车
        self.nav_right_cart = ['id', 'J_MiniCart']
        # 收藏夹
        self.nav_right_J_SiteNavFavor = ['xpath', '//*[@id="J_SiteNavFavor"]']
        # 商品分类
        self.nav_right_catalog = ['xpath', '//*[@id="J_SiteNavCatalog"]/div/a/span']
        # 牵牛卖家中心
        self.nav_right_J_SiteNavSeller = ['id', 'J_SiteNavSeller']
        # 联系客服
        self.nav_right_J_SiteNavService = ['xpath', '//*[@id="J_SiteNavService"]/div[1]/a/span']
        # 网站导航
        self.nav_right_J_SiteNavSitemap = ['xpath', '//*[@id="J_SiteNavSitemap"]/div[1]/a/span[2]']

    @allure.step("step:鼠标悬停中国大陆")
    def move_to_nav_left_location(self):
        """
        鼠标悬停中国大陆
        :return:
        """
        self.move_to_element(self.nav_left_location)

    @allure.step("step:鼠标悬停中国大陆,获取弹出的那一组地区名称")
    def get_nav_left_locations_text(self):
        """
        鼠标悬停中国大陆,获取弹出的那一组地区名称元素
        :return:
        """
        locationsList = []
        eles = self.find_elements(self.nav_left_locations)
        for ele in eles:
            locationsList.append(ele.text)
        return locationsList

    @allure.step("step:检查【亲，请登录】按钮是否显示")
    def isDisplay_nav_left_Login(self):
        """
        检查【亲，请登录】按钮是否显示，显示返回Ture,不显示返回False
        """
        return self.isdispaly(self.nav_left_Login)

    @allure.step("step:点击【亲，请登录】按钮")
    def click_nav_left_Login_btn(self):
        """
        点击【亲，请登录】按钮
        """
        self.click(self.nav_left_Login)

    @allure.step("step:点击【免费注册】按钮")
    def click_nav_left_register_btn(self):
        """
        点击【免费注册】按钮
        :return:
        """
        self.click(self.nav_left_register)

    @allure.step("step:点击【手机逛淘宝】按钮")
    def click_nav_left_taobao_btn(self):
        """
        点击【手机逛淘宝】按钮
        :return:
        """
        self.click(self.nav_left_taobao)

    @allure.step("step:点击【我的淘宝】按钮")
    def click_nav_right_mytaobao_btn(self):
        """
        点击【我的淘宝】按钮
        """
        self.click(self.nav_right_mytaobao)

    @allure.step("step:点击【购物车】按钮")
    def click_nav_right_cart_btn(self):
        """
        点击【购物车】按钮
        :return:
        """
        self.click(self.nav_right_cart)