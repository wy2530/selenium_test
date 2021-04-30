from selenium import webdriver
# import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()  # 驱动

driver.get("https://mail.163.com/")  # 163 首页
driver.implicitly_wait(10)
driver.maximize_window()

# 获取登录框

login_ele = driver.find_element_by_xpath("//div[@id='loginDiv']/iframe")  # 找到iframe

#  https://www.cnblogs.com/yi-xixi/p/10972980.html

driver.switch_to.frame(login_ele)  # 跳转
# ActionChains(driver).click(login_ele).perform()  # 这个语句是不是跟login_ele.click()一样啊

# 定位登录框的位置，并输入
login_input = driver.find_element_by_name("email")
login_input.clear()
login_input.send_keys("wangyang_jocelyn")

password = driver.find_element_by_name("password")
password.clear()
password.send_keys("wy453521")
# 定位登录


try:  # 如果没有跳转才捕捉怎么办
    btn_ele = driver.find_element_by_id("dologin").click()
    print("登录成功")
except:
    print("信息不正确")
    driver.get_screenshot_as_file("./error.png")  # 错误信息截图
finally:
    print("测试完成")
# 判断是否登录成功
# 移入到登录窗口，看有没有浮窗 (hover)
# 有浮窗之后，可以打印 用户名的文本信息
# 如果是的话，测试成功；如果不是，测试不成功

# # 定位
# menu_ele = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div[1]/div/ul/li[1]")
#
# # 将鼠标移动到元素上面
# ActionChains(driver).move_to_element(menu_ele).perform()
#
# # 选中子菜单
# sub_menu_ele = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div[1]/div/div/div[1]/div[1]/div[1]/p/a[2]")
#
# # 点击
# sub_menu_ele.click()
