import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conf.decorator import teststep, teststeps
from conf.base_page import BasePage


class HomePage(BasePage):
    """主界面"""

    @teststeps
    def wait_check_parent_title(self):
        try:
            ele = (By.XPATH, "//android.widget.TextView[contains(@text,'万星在线资源服务')]")
            WebDriverWait(self.driver,15, 0.5).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststeps
    def wait_check_findText(self):
        try:
            ele = (By.XPATH, "//android.widget.TextView[contains(@text,'搜索指定内容')]")
            WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststeps
    def wait_check_title(self):
        try:
            ele = (By.ID, "android:id/text1")
            WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststeps
    def wait_check_button(self):
        try:
            ele = (By.CLASS_NAME, "android.widget.Button")
            WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststeps
    def click_find_icon(self):
        self.driver.find_element_by_accessibility_id("搜索").click()
        time.sleep(2)

    @teststep
    def click_sub(self):
        """点开公众号 的text为依据"""
        self.click_find_icon()
        if self.wait_check_findText():
            find_ele = self.find_exp()
            find_ele.send_keys(u'万星')
            if self.wait_check_parent_title():
                self.driver.find_element_by_xpath(
                    '//android.widget.TextView[contains(@text,"万星在线资源服务")]').click()
                time.sleep(3)
            else:
                print("未发现公众号元素")

    @teststep
    def find_exp(self):
        find_ele = self.driver.find_element_by_id('com.tencent.mm:id/jd')
        return find_ele


    @teststep
    def report_tab(self):
        """点公众号菜单- 学习报告 的xpath为依据"""
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/af8"]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]').click()
        time.sleep(3)


    @teststep
    def buy_tab(self):
        """点公众号菜单- 购买”的xpath为依据"""
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/af8"]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]').click()
        time.sleep(5)

    @teststep
    def account_tab(self):
        """点公众号菜单- 我的账号的text为依据"""
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/af8"]/android.widget.FrameLayout[3]/android.widget.LinearLayout[1]').click()

    @teststep
    def cancel_button(self):
        """以“返回按钮”的id为依据"""
        self.driver \
            .find_element_by_name("取消").click()

    @teststep
    def get_text1(self):
        """获取页面标题"""
        ele = self.driver.find_element_by_id("android:id/text1")
        return ele.text

    @teststep
    def back_to_club_home(self):
        """以“返回按钮”的id为依据"""
        time.sleep(2)
        self.driver.find_element_by_id("com.tencent.mm:id/j8").click()

    @teststep
    def back_to_find(self):
        """以“返回按钮”的id为依据"""
        self.driver \
            .find_element_by_id("com.tencent.mm:id/iz").click()
        time.sleep(2)

    @teststeps
    def back_to_wx_home(self):
        """点击左上角返回键"""
        if self.wait_check_parent_title():
            self.driver.find_element_by_id("com.tencent.mm:id/ja").click()
            time.sleep(3)

    @teststeps
    def back_to_mainPage(self):
        """退回至微信主页面"""
        self.back_to_club_home()
        if self.wait_check_parent_title():
            self.back_to_find()
            if self.wait_check_parent_title():
                self.back_to_wx_home()

    # 未登录状态时
    @teststeps
    def wait_check_login_page(self):
        """以title：“登录”的text为依据"""
        try:
            locator = (By.XPATH, "//android.widget.TextView[contains(@text,'登录')]")
            WebDriverWait(self.driver, 25, 0.5).until(EC.presence_of_element_located(locator))
            return True
        except:

            return False


    @teststeps
    def wait_check_has_logined_page(self):
        """以title：“登录”的text为依据"""
        try:
            locator = (By.XPATH, "//android.widget.TextView[contains(@text,'退出登录')]")
            WebDriverWait(self.driver, 25, 0.5).until(EC.presence_of_element_located(locator))
            return True
        except:

            return False

    @teststep
    def ele_input_text(self):
        """手机哈 密码 输入框的text为依据"""
        inputs = self.driver.find_elements_by_class_name('android.widget.EditText')
        return inputs

    @teststep
    def login_button(self):
        """登录 button的text为依据"""
        self.driver.find_element_by_class_name("android.widget.Button").click()

    @teststep
    def show_password(self):
        """显示密码 的text为依据"""
        self.driver.find_element_by_xpath('//*[@resource-id="app"]/android.view.View[2]/'
                                          'android.view.View[3]/android.view.View[4]').click()
        time.sleep(2)


    def page_source(self):
        """以“获取page_source”的TEXT为依据"""
        print('打开：', self.driver.page_source)

    @teststeps
    def login_operate(self, username, password):
        if self.wait_check_login_page():  # 页面检查点
            phone = self.login_phone()
            pwd = self.login_password()

            phone.click()  # 激活phone输入框
            phone.send_keys(username)  # 输入手机号

            pwd.click()  # 激活pwd输入框
            pwd.send_keys(password)  # 输入密码

            self.login_button()
            if self.wait_check_login_page():
                print('登录失败', username)
