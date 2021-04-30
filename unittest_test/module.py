"""
unittest框架由哪几个部分组成？

test fixture（测试脚手架）——测试代码的运行环境，指测试准备前和执行后要做的工作，包括setUp()和tearDown()；
TestCase（测试案例）——所有测试用例的基类，它是软件测试中最基本的组成单元；
TestSuite（测试套件）——测试案例的集合；
test runner（执行测试）——测试用例的执行


请参照下列被测程序段，利用unittest框架编写测试用例。请使用TestCase，TestSuite，TestRunner的方式运行。

:
    (,a,b):
        .a = (a)
        .b = (b)
    ():
        .a + .b
    ():
        .a - .b
    ():
        .a * .b
    ():
        .a / .b
"""


class Calculator():
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b
