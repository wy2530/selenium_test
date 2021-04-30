import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("file:///D:/mycode/Selenium_test/learning_test/4_2.html")  # 需要在文件上面复制 绝对路径

print(driver.title)

print("默认选中male")

# 事件4：选择另一个单选框
time.sleep(2)
driver.find_element_by_id("female").click()

# 弹窗处理
time.sleep(2)

driver.find_element_by_id("alert").click()
# 切换到弹窗
win_ele = driver.switch_to.alert()  # switch_to_alert() 换成了switch_to.alert()
time.sleep(2)
win_ele.accept()

driver.find_element_by_id("confirm").click()
win = driver.switch_to.alert()
# win.accept()  # 确定
win.dismiss()  # 取消
