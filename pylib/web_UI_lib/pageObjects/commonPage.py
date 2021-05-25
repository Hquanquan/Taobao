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
    # 中国大陆
    nav_left_location = ["css selector", "#J_SiteNavBd .site-nav-menu-hd .site-nav-region"]
    # 中国大陆  一组元素
    nav_left_locations = ["xpath", '//*[@id="J_SiteNavRegionList"]/li[1]']

    @allure.step("step:鼠标悬停中国大陆")
    def move_to_nav_left_location(self):
        """
        鼠标悬停中国大陆
        :return:
        """
        self.move_to_element(self.nav_left_location)

    def test(self):
        self.click(self.nav_left_locations)



