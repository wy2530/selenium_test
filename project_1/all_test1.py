import unittest
import HTMLTestRunner
import category
from project_1 import login
import time


# 创建测试集合
def creat_suite():
    print("开始测试")
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(login.类名))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(category.类名))
    return suite


if __name__ == '__main__':
    suite = creat_suite()
    # 在测试报告中加入了时间
    file_prefix = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    print(file_prefix)
    # wb：二进制格式打开文件
    fp = open("./" + file_prefix + "_result.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="测试报告", description="测试报告")
    runner.run(suite)
    fp.close()

"""
　过去都是用 
　　　　suite = unittest.makeSuite(HelloTestCase)
　　建立完整的TestSuite。


升级到Python3后，发现makeSuite没有啦！其实是被下面这段代码取代了。
　　　　suite=unittest.TestLoader().loadTestsFromTestCase(HelloTestCase)

　　　　(备注: TestLoader uses the 'test' method name prefix to identify test methods automatically.)
"""