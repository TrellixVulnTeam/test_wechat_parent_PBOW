#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
import unittest
import os

import time

from selenium.webdriver.common.by import By


from app.wechat_subscription.object_page.home_page import HomePage
from app.wechat_subscription.object_page.login_page import LoginPage
from app.wechat_subscription.object_page.report_page import ReportPage
from app.wechat_subscription.object_page.mine_account_page import AccountPage
from app.wechat_subscription.object_page.order_page import OrderPage
from app.wechat_subscription.test_data.mine_account import phone_data
from conf.decorator import testcase, setup, teardown, teststeps



PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))  # 获取当前路径


class Account(unittest.TestCase):
    """登录测试 - 手机号"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.home = HomePage()
        cls.login = LoginPage()
        cls.report = ReportPage()
        cls.order = OrderPage()
        cls.account = AccountPage()


    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_login_phone(self):
        print("\n\n---验证登录脚本---\n\n")
        self.login.app_status()  # 判断APP当前状态
        self.home.click_sub()  # 进入公众号
        if self.home.wait_check_parent():  # 页面检查点
            self.home.account_tab()
            self.account.mine_account()

            if self.home.wait_check_login_page():
                print("用户未登录，进行登录校验操作")
                self.login_operate_phone()  # 测试手机号
            elif self.account.wait_check_account():
                print("已登录，退出重新登录")
                self.account.logout_operate()  # 退出登录
                if self.home.wait_check_login_page():  # 页面检查点
                    self.login_operate_phone()  # 测试手机号
            else:
                print("ERROR！页面标题不正确！")
            self.home.back_to_mainPage()  # 返回主界面
    @teststeps
    def login_operate_phone(self):
        """登录 操作流程 - 测试手机号"""
        for i in range(0,len(phone_data),3):
            if not self.home.wait_check_button():  # 判断是否恢复内核
                self.login.clear_tbs_to_retry()
                self.home.account_tab()
                self.account.mine_account()
            print(" ")
            self.login_pwd(i)

    @teststeps
    def login_pwd(self,i):
        if self.home.wait_check_login_page():  # 页面检查点

            phone = self.home.login_phone()
            pwd = self.home.login_password()

            phone.click()  # 激活phone输入框
            phone.send_keys(phone_data[i]['username'])  # 输入手机号

            pwd.click()  # 激活pwd输入框
            # self.home.show_password()
            pwd.send_keys(phone_data[i]['password'])  # 输入密码

            self.home.login_button()
            self.login.check_login_error_info()
            if self.home.wait_check_login_page():
                print('登录失败', phone_data[i]['username'])
                self.home.back_to_club_home()  # 点击关闭按钮
                if HomePage().wait_check_parent():
                    if i == 0:
                        self.home.report_tab()  # 点击底部菜单 - 学习报告
                        self.report.study_month_report()  # 点击二级标题 学习月报
                    elif i in (1, 3):
                        self.home.report_tab()  # 点击底部菜单 - 学习报告
                        self.report.study_week_report()  # 点击二级标题 学习周报
                    elif i == 4:
                        self.home.buy_tab()  # 点击底部菜单 - 购买
                    elif i == 5:
                        self.home.account_tab()  # 点击底部菜单 - 账号管理
                        self.order.mine_order()  # 点击二级标题 我的订单
                    else:
                        self.home.account_tab()  # 点击底部菜单 - 账号管理
                        self.account.mine_account()  # 点击二级标题 我的账号
            else:
                print('登录成功：',phone_data[i]['username'])
                self.account.logout_operate()
        print('----------------------------------')
