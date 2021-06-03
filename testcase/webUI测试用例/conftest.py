#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 13:34
# @Author  : 黄权权
# @File    : conftest.py
# @Software: PyCharm
import pytest

from pylib.web_UI_lib.pageObjects.commonPage import CommonPage
from pylib.web_UI_lib.pageObjects.consumerServicePage import ConsumerServicePage
from pylib.web_UI_lib.pageObjects.downloadPage import DownloadPage
from pylib.web_UI_lib.pageObjects.homePage import HomePage
from pylib.web_UI_lib.pageObjects.loginPage import LoginPage
from pylib.web_UI_lib.pageObjects.marketPage import MarketPage
from pylib.web_UI_lib.pageObjects.openShopPage import OpenShopPage
from pylib.web_UI_lib.pageObjects.registerPage import RegisterPage
from pylib.web_UI_lib.pageObjects.siteMapPage import SiteMapPage


@pytest.fixture(scope="session")
def init_commonPage():
    """
    初始化创建一个commomPage 实例对象
    :return: 
    """
    commonPage = CommonPage()
    yield commonPage
    # 关闭浏览器
    # commonPage.quit_browser()

@pytest.fixture(scope="session")
def init_homePage():
    """
    初始化创建一个homePage 实例对象
    :return:
    """
    homePage = HomePage()
    yield homePage

@pytest.fixture(scope="session")
def init_loginPage():
    """
    初始化创建一个loginPage 实例对象
    :return:
    """
    loginPage = LoginPage()
    yield loginPage


@pytest.fixture(scope="session")
def init_registerPage():
    """
    初始化创建一个registerPage 实例对象
    :return:
    """
    registerPage = RegisterPage()
    yield registerPage


@pytest.fixture(scope="session")
def init_downloadPage():
    """
    初始化创建一个downloadPage 实例对象
    :return:
    """
    downloadPage = DownloadPage()
    yield downloadPage


@pytest.fixture(scope="session")
def init_marketPage():
    """
    初始化创建一个marketPage 实例对象
    :return:
    """
    marketPage = MarketPage()
    yield marketPage


@pytest.fixture(scope="session")
def init_openShopPage():
    """
    初始化创建一个openShopPage 实例对象
    :return:
    """
    openShopPage = OpenShopPage()
    yield openShopPage

@pytest.fixture(scope="session")
def init_consumerServicePage():
    """
    初始化创建一个consumerServicePage 实例对象
    :return:
    """
    consumerServicePage = ConsumerServicePage()
    yield consumerServicePage

@pytest.fixture(scope="session")
def init_siteMapPage():
    """
    初始化创建一个siteMapPage 实例对象
    :return:
    """
    siteMapPage = SiteMapPage()
    yield siteMapPage

