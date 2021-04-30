from selenium import webdriver
import time, unittest
from selenium.webdriver.common.action_chains import ActionChains


class loginTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()  # 驱动
        self.driver.get("https://www.baidu.com")  # 百度首页
        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        time.sleep(5)  # 三秒
        self.driver.quit()

    def test_1(self) -> None:
        u"""找到163邮箱官网"""
        driver = self.driver
        driver.find_element_by_id("kw").send_keys("163 邮箱")  # 搜索官网网址
        driver.find_element_by_id("su").click()

        driver.find_element_by_xpath("//*[@id='1']/h3/a[1]").click()  # 找到官网并点击

        # 定位用户名的位置，并输入   注意：163邮箱的登录框在一个iframe中

        # 定位到对应的frame
        # driver.find_element_by_id('switchAccountLogin').click()
        iframe = driver.find_element_by_xpath('//*[@id="loginDiv"]/iframe')  # 使用Xpath选定位到iframe
        driver.switch_to.frame(iframe)



        user_name = driver.find_element_by_name("email")
        user_name.clear()
        user_name.send_keys("wangyang_jocelyn")

        pwd = driver.find_element_by_name("password")
        pwd.clear()
        pwd.send_keys("wy453521")
        #
        # try:  # 如果没有跳转才捕捉怎么办
        #     btn_ele = driver.find_element_by_xpath("//*[@id='login-form']/div[4]/buttton").click()
        #     print("登录成功")
        # except:
        #     print("信息不正确")
        #     driver.get_screenshot_as_file("./error.png")  # 错误信息截图
        # finally:
        #     print("测试完成")


if __name__ == '__main__':
    unittest.main()  # 可以直接测试
