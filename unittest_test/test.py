import unittest  # 导入单元测试框架
from unittest_test.module import Calculator


class ModuleTest(unittest.TestCase):  # 创建ModuleTest类继承unittest.TestCase类
    # 测试用例执行前的初始化
    def setUp(self):
        self.cal = Calculator(10, 2)

    # 测试用例执行之后的善后工作
    def tearDown(self):
        pass

    # 测试用例（方法）必须以test开头
    def test_add(self):
        result = self.cal.add()
        self.assertAlmostEqual(result, 12)  # 断言

    def test_sub(self):
        result = self.cal.sub()
        self.assertAlmostEqual(result, 8)

    def test_mul(self):
        result = self.cal.mul()
        self.assertAlmostEqual(result, 20)

    def test_div(self):
        result = self.cal.div()
        self.assertAlmostEqual(result, 5)


if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(ModuleTest("test_add"))
    suite.addTest(ModuleTest("test_sub"))
    suite.addTest(ModuleTest("test_mul"))
    suite.addTest(ModuleTest("test_div"))

    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)