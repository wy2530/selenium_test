import unittest
import HTMLTestRunner
from homework import category
from homework import login_order
from homework import mail

# 创建测试集合
def create_suite():
    print("测试开始")
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(login_order.LoginOrderTestCase))
    suite.addTest(unittest.makeSuite(category.CategoryTestCase))
    return suite


if __name__ == '__main__':
    suite = create_suite()
    # 创建测试报告，此时这个文件还是空文件 wb 以二进制格式打开一个文件，只用于写入，如果文件存在则覆盖，不存在则创建
    fp = open("./result.html", "wb")
    # stream定义一个测试报告写入的文件，title就是标题，description就是描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"小D课堂 测试报告", description=u"测试用例执行情况", verbosity=2)
    runner.run(suite)
    fp.close()
    # 将测试报告由邮件发出
    mail.MailUtils.send_test_report()
