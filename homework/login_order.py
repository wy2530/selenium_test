import unittest
import time
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


class LoginOrderTestCase(unittest.TestCase):
    def setUp(self):
        print("测试开始")
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)   # 等待时间
        self.base_url = "https://xdclass.net"  # 小D课题官网首页
        self.driver.get(self.base_url)
        self.driver.maximize_window()    # 最大化窗口

    def tearDown(self):
        print("单个测试用例结束")   # 单个测试用例结束

    def test_login_order(self):
        u"""登录测试用例"""
        driver = self.driver
        # 登录框
        login_ele = driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div/div[4]/div[3]/span[2]")
        ActionChains(driver).click(login_ele).perform()
        sleep(5)

        # 查找输入框,输入账号，输入框要提前清理里面的数据
        login = driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div/div[2]/div[2]/div/div[1]/input")
        login.clear()
        login.send_keys("15081983129")
        # 查找密码输入框，输入密码
        pwd = driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div/div[2]/div[2]/div/div[2]/input")
        pwd.clear()
        pwd.send_keys("wy453521")

        # 拿到登录按钮
        login_btn_ele = driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div/div[2]/div[2]/div/div[3]/button")
        # 触发点击事件,登录
        login_btn_ele.click()
        # 判断登陆是否成功，逻辑-》鼠标移到上面，判断弹窗字符

        # 获取鼠标上移的元素
        user_info_ele = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[4]/div[5]/img')
        sleep(2)
        # hover触发
        ActionChains(driver).move_to_element(user_info_ele).perform()
        sleep(1)
        # 获取用户名称元素
        user_name_ele = driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div/div[6]/div/div/div[1]/p")
        print("===hover:登录测试结果==")
        print(user_name_ele.text)
        # # 测试成功后进入下单页面
        # name = user_name_ele.text

        sleep(5)


        video_ele = driver.find_element_by_xpath("//*[@id='app']/div/div[3]/div/div[2]/a[1]/div")
        video_ele.click()

        # 进入新页面后，转换句柄
        time.sleep(2)
        handles = driver.window_handles  # 获取当前浏览器所有窗口句柄
        driver.switch_to.window(handles[-1])  # 切换最新窗口句柄

        btn=driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[2]/div[2]/div[1]/div[1]/a')
        btn.click()

        time.sleep(10)
        print("进入下单页面")


if __name__ == '__main__':
    unittest.main()

