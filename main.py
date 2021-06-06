#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 13:55
# @Author  : 黄权权
# @File    : main.py
# @Software: PyCharm
import os

import pytest

from pylib.web_UI_lib.pageObjects.commonPage import CommonPage


def run():
    """
    运行测试，并且启动服务
    """
    for one in os.listdir('report/tmp'):  # 列出对应文件夹的数据
        if 'json' in one:
            os.remove(f"report/tmp/{one}")
    pytest.main(['testcase/webUI测试用例', '-s', '--alluredir=report/tmp'])
    os.system('allure serve report/tmp')


if __name__ == '__main__':
    # run()

    # pytest.main(["-s", "-k test_isDisplay_nav_left_Login"])

    # 运行被标记有test的测试用例
    pytest.main(["-s", "-m", "test"])

    # c = CommonPage()
    # c.move_to_nav_left_location()
    # l = c.get_nav_left_locations_text()
    # print(l)
    