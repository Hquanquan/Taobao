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
        self.nav__left_Login = ["xpath", '//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]']
        # 点击免费注册
        self.nav_left_register = ['xpath', '//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[2]']
        # 用户名称(已登录时)
        self.nav__left_user = ['xpath', '//*[@id="J_SiteNavLogin"]/div[1]/div[2]']
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

    def test_001(self):
        # self.click(self.nav_left_locations)
        mylist = []
        eles = self.find_elements(self.nav_left_locations)
        for ele in eles:
            print(ele.text)
            mylist.append(ele.text)
        return mylist
