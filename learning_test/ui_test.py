import unittest
import HTMLTestRunner
import time


class UserTestCase(unittest.TestCase):
    # 类的初始化
    @classmethod
    def setUpClass(cls) -> None:
        print("111")

    # 类的释放
    @classmethod  # 需要加装饰器
    def tearDownClass(cls) -> None:
        print("222")

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    # 函数(不是test开头的，不会识别，但可以调用)
    def plus(self, a, b):
        print(a + b)

    # 测试用例
    # @unittest.skip("不想执行")
    def test_a(self):
        self.plus(1, 2)  # 调用
        print("test_a")

    def test_c(self):
        # self.assert
        print("test_c")

    # @unittest.skipIf("条件","理由")
    # @unittest.skipUnless()
    # @unittest.expectedFailure
    def test_b(self):
        print("test_b")


if __name__ == '__main__':
    # unittest.main()   # 可以直接测试
    suite = unittest.TestSuite()
    # 可以控制用例的顺序
    suite.addTest(UserTestCase("test_c"))
    suite.addTest(UserTestCase("test_a"))

    # # verbosity参数可以控制执行结果的输出，0是简单报告，1是一般报告(默认的) 2是详细报告
    # runner = unittest.TextTestRunner(verbosity=0)
    # runner.run(suite)  # 运行容器中的测试集

    # 在测试报告中加入了时间
    file_prefix = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    print(file_prefix)
    # wb：二进制格式打开文件
    fp = open("./" + file_prefix + "_result.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="测试报告", description="测试报告")
    runner.run(suite)
    fp.close()
