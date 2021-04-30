from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()  # 驱动

driver.get("https://www.taobao.com/")  # 淘宝首页

# 定位
menu_ele = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div[1]/div/ul/li[1]")

time.sleep(3)
# 将鼠标移动到元素上面
ActionChains(driver).move_to_element(menu_ele).perform()

# 选中子菜单
sub_menu_ele = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div[1]/div/div/div[1]/div[1]/div[1]/p/a[2]")
time.sleep(3)
# 点击
sub_menu_ele.click()



