import unittest
import time
from selenium import webdriver

from ddt import ddt, data, unpack, file_data
import yaml


def readFile():
    params = []
    with open("params. txt", mode='r', encoding='utf-8') as f:
        for line in f:
            # res = f.read(line.split(','))
            params.append(line.split(','))
    return params


@ddt
class userTestCase(unittest.TestCase):
    # def setUp(self) -> None:
    #     self.driver = webdriver.Chrome()
    #     self.driver.get("http://www.baidu.com")

    # def tearDown(self) -> None:
    #     time.sleep(5)
    #     self.driver.quit()

    # def test_1(self) -> None:
    #     self.driver.find_element_by_id("kw").send_keys("自动化测试")
    #     self.driver.find_element_by_id("su").click()
    #
    # def test_2(self) -> None:
    #     self.driver.find_element_by_id("kw").send_keys("自动化测试")
    #     self.driver.find_element_by_id("su").click()

    # 目前test_1,test_2只有传入的参数不一样，那么我们再次简化代码 使用ddt装饰器
    # @data(("你好","自动化"),)
    # @data(*readFile())  # 对测试用例的参数进行调用
    # @unpack
    # def test_1(self, txt) -> None:
    #     self.driver.find_element_by_id("kw").send_keys(txt)
    #     self.driver.find_element_by_id("su").click()

    # # 如果有两个参数
    # @data(('自动化', '文本'), ('hello', 'world'))
    # @unpack
    # def test_2(self, txt, value) -> None:
    #     self.driver.find_element_by_id("kw").send_keys(txt)
    #     print(value)
    #     self.driver.find_element_by_id("su").click()

    @file_data('ppp.yml')
    def test_3(self, txt):
        print(txt)


if __name__ == '__main__':
    unittest.main()
