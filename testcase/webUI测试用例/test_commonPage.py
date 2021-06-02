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
        鼠标移入【中国大陆】,弹出13个地区名称列表
        :param init_commonPage:
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
        assert result is True

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
        验证未登录时，点击【手机逛淘宝】按钮，跳转到PC下载页,后置处理：返回上一页
        :param init_commonPage:
        :param init_downloadPage:
        """
        self.commonPage = init_commonPage
        self.downloadPage = init_downloadPage
        yield
        self.downloadPage.back_browser()

    # @pytest.mark.test
    @allure.story("顶部导航栏左侧按钮功能测试")
    @allure.title("验证未登录时，点击【手机逛淘宝】按钮，跳转到PC下载页")
    def test_click_nav_left_taobao_btn(self, after_test_click_nav_left_taobao_btn):
        """
        验证未登录时，点击【手机逛淘宝】按钮，跳转到PC下载页
        :param after_test_click_nav_left_taobao_btn:
        :return:
        """
        # 点击【手机逛淘宝】按钮
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

    @allure.story("顶部导航栏左侧按钮功能测试")
    @allure.title("验证鼠标移入【我的淘宝】")
    def test_move_to_nav_right_mytaobao(self, init_commonPage):
        """
        验证鼠标移入【我的淘宝】,弹出一组数据
        :param init_commonPage:
        :return:
        """
        self.commonPage = init_commonPage
        # 鼠标移入【我的淘宝】
        self.commonPage.move_to_nav_right_mytaobao()
        # 获取弹出的那一组数据的文本值
        text = self.commonPage.get_nav_right_mytaobao_lists_text()
        assert text == ['已买到的宝贝', '我的足迹']

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

    # @pytest.mark.test
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
        # 获取登录页面特有文案
        text = self.loginPage.get_login_text()
        assert text == "密码登录"

    # @pytest.mark.test
    @allure.story("顶部导航栏左侧按钮功能测试")
    @allure.title("验证鼠标移入【收藏夹】")
    def test_move_to_nav_right_J_SiteNavFavor(self, init_commonPage):
        """
        验证鼠标移入【收藏夹】,弹出一组数据
        :param init_commonPage:
        :return:
        """
        self.commonPage = init_commonPage
        # 鼠标移入【收藏夹】
        self.commonPage.move_to_nav_right_J_SiteNavFavor()
        # 获取弹出的那一组数据的文本值
        text = self.commonPage.get_nav_right_J_SiteNavFavor_lists_text()
        print(text)
        assert text == ['收藏的宝贝', '收藏的店铺']

    @pytest.fixture()
    def after_test_click_nav_right_J_SiteNavFavor(self, init_commonPage, init_loginPage):
        """
        验证未登录时，点击【收藏夹】按钮，跳转到登录页,后置处理，返回上一页
        :param init_commonPage:
        :param init_loginPage:
        """
        self.commonPage = init_commonPage
        self.loginPage = init_loginPage
        yield
        self.loginPage.back_browser()

    # @pytest.mark.test
    @allure.story("顶部导航栏左侧按钮功能测试")
    @allure.title("验证未登录时，点击【收藏夹】按钮，跳转到登录页")
    def test_click_nav_right_J_SiteNavFavor(self, after_test_click_nav_right_J_SiteNavFavor):
        """
        验证未登录时，点击【收藏夹】按钮，跳转到登录页
        :param after_test_click_nav_right_J_SiteNavFavor:
        :return:
        """
        # 点击【收藏夹】
        self.commonPage.click_nav_right_J_SiteNavFavor()
        # 跳转到登录页
        # 获取登录页面特有文案
        text = self.loginPage.get_login_text()
        assert text == "密码登录"

    @pytest.fixture()
    def after_test_click_nav_right_catalog(self, init_commonPage, init_marketPage):
        """
        验证点击【商品分类】按钮，跳转到商品分类市场页,后置处理：返回上一页
        :param init_commonPage:
        :param init_marketPage:
        """
        self.commonPage = init_commonPage
        self.marketPage = init_marketPage
        yield
        self.marketPage.back_browser()

    # @pytest.mark.test
    @allure.story("顶部导航栏左侧按钮功能测试")
    @allure.title("验证点击【商品分类】按钮，跳转到商品分类市场页")
    def test_click_nav_right_catalog(self, after_test_click_nav_right_catalog):
        """
        验证点击【收藏夹】按钮，跳转到商品分类市场页
        :param after_test_click_nav_right_catalog:
        :return:
        """
        # 点击【商品分类】
        self.commonPage.click_nav_right_catalog()
        # 跳转到商品分类市场页
        title = self.marketPage.get_url_title()
        assert title == "淘宝首页行业市场"

    @pytest.fixture()
    def after_test_click_J_SiteNavFree(self, init_commonPage, init_openShopPage):
        """
        验证点击【免费开店】按钮，跳转到新商家开店页,后置处理：返回上一页
        :param init_commonPage:
        :param init_openShopPage:
        :return:
        """
        self.commonPage = init_commonPage
        self.openShopPage = init_openShopPage
        yield
        self.openShopPage.back_browser()

    # @pytest.mark.test
    @allure.story("顶部导航栏左侧按钮功能测试")
    @allure.title("验证点击【免费开店】按钮，跳转到新商家开店页")
    def test_click_J_SiteNavFree(self, after_test_click_J_SiteNavFree):
        """
        验证点击【免费开店】按钮，跳转到新商家开店页
        :param after_test_click_J_SiteNavFree:
        :return:
        """
        # 点击免费开店
        self.commonPage.click_J_SiteNavFree()
        # 跳转到新商家开店页
        # 获取新商家开店页的title
        title = self.openShopPage.get_url_title()
        assert title == "新商家开店"

    # @pytest.mark.test
    @allure.story("顶部导航栏左侧按钮功能测试")
    @allure.title("验证鼠标移入【牵牛卖家中心】")
    def test_move_to_nav_right_J_SiteNavSeller(self, init_commonPage):
        """
        验证鼠标移入【牵牛卖家中心】
        :param init_commonPage:
        :return:
        """
        self.commonPage = init_commonPage
        # 鼠标移入【牵牛卖家中心】
        self.commonPage.move_to_nav_right_J_SiteNavSeller()
        # 获取弹出的那一组元素的文本值
        text = self.commonPage.get_nav_right_J_SiteNavSeller_lists_text()
        assert text == ['免费开店', '已卖出的宝贝', '出售中的宝贝', '卖家服务市场', '卖家培训中心', '体检中心', '问商友']

    @pytest.fixture()
    def after_test_click_nav_right_J_SiteNavSeller(self, init_commonPage, init_loginPage):
        """
        未登录状态，验证点击【牵牛卖家中心】，跳转到登录页,后置处理：返回上一页
        :param init_commonPage:
        :param init_loginPage:
        :return:
        """
        self.commonPage = init_commonPage
        self.loginPage = init_loginPage
        yield
        self.loginPage.back_browser()

    # @pytest.mark.test
    @allure.story("顶部导航栏左侧按钮功能测试")
    @allure.title("未登录状态，验证点击【牵牛卖家中心】，跳转到登录页")
    def test_click_nav_right_J_SiteNavSeller(self, after_test_click_nav_right_J_SiteNavSeller):
        """
        未登录状态，验证点击【牵牛卖家中心】，跳转到登录页
        :param after_test_click_nav_right_J_SiteNavSeller:
        :return:
        """
        # 点击【牵牛卖家中心】
        self.commonPage.click_nav_right_J_SiteNavSeller()
        # 跳转到登录页
        # 获取登录页特有文案
        # 获取登录页面特有文案
        text = self.loginPage.get_login_text()
        assert text == "密码登录"

    # @pytest.mark.test
    @allure.story("顶部导航栏左侧按钮功能测试")
    @allure.title("验证鼠标移入【联系客服】")
    def test_move_to_nav_right_J_SiteNavService(self, init_commonPage):
        """
        验证鼠标移入【联系客服】,弹出一组元素
        :param init_commonPage:
        :return:
        """
        self.commonPage = init_commonPage
        # 验证鼠标移入【联系客服】
        self.commonPage.move_to_nav_right_J_SiteNavService()
        # 获取弹出的那一组元素的文本值
        text = self.commonPage.get_nav_right_J_SiteNavService_lists_text()
        assert text == ['消费者客服', '商家服务大厅']

    @pytest.fixture()
    def after_test_click_nav_right_J_SiteNavService(self, init_commonPage,  init_consumerServicePage):
        """
        验证点击【联系客服】，跳转到客户服务中心页,后置处理：返回上一页
        :param init_commonPage:
        :param init_consumerServicePage:
        :return:
        """
        self.commonPage = init_commonPage
        self.consumerServicePage = init_consumerServicePage
        yield
        self.consumerServicePage.back_browser()

    # @pytest.mark.test
    @allure.story("顶部导航栏左侧按钮功能测试")
    @allure.title("验证点击【联系客服】，跳转到客户服务中心页")
    def test_click_nav_right_J_SiteNavService(self, after_test_click_nav_right_J_SiteNavService):
        """
        验证点击【联系客服】，跳转到客户服务中心页
        :param after_test_click_nav_right_J_SiteNavService:
        :return:
        """
        # 点击【联系客户】
        self.commonPage.click_nav_right_J_SiteNavService()
        # 跳转到客户服务中心页
        title = self.consumerServicePage.get_url_title()
        assert title == "服务中心"

    # @pytest.mark.test
    @allure.story("顶部导航栏左侧按钮功能测试")
    @allure.title("验证鼠标移入【网站导航】后,是否显示的部分导航元素")
    def test_isDisplay_J_SiteMapBd(self, init_commonPage):
        """
        验证鼠标移入【网站导航】后,是否显示的部分导航元素
        :return:
        """
        self.commonPage = init_commonPage
        # 验证鼠标移入【网站导航】
        self.commonPage.move_to_nav_right_J_SiteNavSitemap()
        # 判断是否显示的部分导航元素
        flag = self.commonPage.isDisplay_J_SiteMapBd()
        assert flag is True

    @pytest.fixture()
    def after_test_click_nav_right_J_SiteNavSitemap(self, init_commonPage, init_siteMapPage):
        """
        验证点击【网站导航】，跳转到网站导航页，后置处理：返回上一页
        :param init_commonPage:
        :param init_siteMapPage:
        :return:
        """
        self.commonPage = init_commonPage
        self.siteMapPage = init_siteMapPage
        yield
        self.siteMapPage.back_browser()

    @pytest.mark.test
    @allure.story("顶部导航栏左侧按钮功能测试")
    @allure.title("验证点击【网站导航】，跳转到网站导航页")
    def test_click_nav_right_J_SiteNavSitemap(self, after_test_click_nav_right_J_SiteNavSitemap):
        """
        验证点击【网站导航】，跳转到网站导航页
        :param after_test_click_nav_right_J_SiteNavSitemap:
        :return:
        """
        # 点击【网站导航】
        self.commonPage.click_nav_right_J_SiteNavSitemap()
        # 跳转到网站导航页
        title = self.siteMapPage.get_url_title()
        assert title == "网址导航"


















