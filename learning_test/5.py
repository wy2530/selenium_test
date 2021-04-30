import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("file:///D:/mycode/Selenium_test/learning_test/4_2.html")  # 需要在文件上面复制 绝对路径

print(driver.title)

time.sleep(2)

#  Cooike
driver.add_cookie({"name": "name", "value": " jack"})

# 手动把cookie添加进去
#  token value



