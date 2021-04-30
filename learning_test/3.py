from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://baidu.com")

try:
    # 显性等待
    ele = WebDriverWait(driver, 5, 0, 5).until(EC.presence_of_element_located((By.ID, "kw1")))

    ele.send_keys("自动化测试")

    print("资源加载成功")
except:
    print("资源加载失败")

finally:  # 无论是否成功，都会执行
    # driver.close()
    print("错了")
print(driver.title)
