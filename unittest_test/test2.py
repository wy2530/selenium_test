"""
通过CSS定位元素：
（1）利用ID定位“必应”首页，国内版输入框，并输入“自动化测试”后，利用CLASS定位到搜索按钮并点击。

（2）利用属性定位“必应”首页左上角的“学术”，进入后利用组合定位找到新页面的输入框，并输入“selenium”，利用任意方法定位搜索按钮并点击。

将以上功能的完整代码上交。直接粘贴，提交即可。不要上交WORD或者PY源文件。
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# import time

driver = webdriver.Chrome('D:\chromedrive\chromedriver.exe')  # 驱动
driver.get("https://cn.bing.com/?FORM=BEHPTB")  # 打开页面

element = driver.find_element_by_css_selector("#scpl2").click()  # 属性定位到"学术"并点击
# time.sleep(2)

element_new = driver.find_element_by_xpath("//input[@class='b_searchbox']")
element_new.send_keys("selenium")
# time.sleep(2)
driver.find_element_by_class_name("b_searchboxSubmit").click()  # css定位到搜索，并点击




