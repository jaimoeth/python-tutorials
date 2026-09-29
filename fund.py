# 1.注释
# "#" 用于单行注释
# 多行注释可以使用三个引号（''' 或 """）包裹起来
# 2. 变量
# 变量是用于存储数据的容器，可以是数字、字符串、列表等
# 变量名可以包含字母、数字和下划线，但不能以数字开头
# 3. 数据类型
# Python 中常见的数据类型包括：
# - 整数（int）：用于表示整数值，例如 1、-5、 0
# - 浮点数（float）：用于表示小数值，例如 3.14、-0.5
# - 字符串（str）：用于表示文本，例如 "Hello, World!"、'Python'
# - 布尔值（bool）：用于表示真或假，只有两个取值 True 和 False
# - 列表（list）：用于存储一组有序的元素，可以包含不同类型的数据，例如 [1, 2, 3]、['apple', 'banana', 'cherry']
# - 元组（tuple）：用于存储一组有序的元素，与列表类似，但不可修改，例如 (1, 2, 3)、('apple', 'banana', 'cherry')
# - 字典（dict）：用于存储键值对的数据结构，例如 {'name': 'Alice', 'age': 25}、{'fruit': 'apple', 'color': 'red'}
# - 集合（set）：用于存储一组唯一的元素，例如 {1, 2, 3}、{'apple', 'banana', 'cherry'}
# 4. 运算
# Python 支持各种运算符，包括：
# - 算术运算符：+、-、*、/、//（取整除）、%（取余）、**（幂运算）
# - 比较运算符：==、!=、>、<、>=、<=
# - 逻辑运算符：and、or、not
# - 赋值运算符：=、+=、-=、*=、/=、//=、%=、**=
# 5. 控制流
# Python 提供了多种控制流语句，包括：
# - 条件语句：if、elif、else
# - 循环语句：for、while
# - 跳转语句：break、continue、pass 
# 6. 函数
# 函数是用于封装一段可重复使用的代码块，可以接受参数并返回结果。函数的定义使用 def 关键字，例如：
def greet(name):
    """打印问候语"""
    print(f"Hello, {name}!")
# 7. 模块
# 模块是一个包含 Python 代码的文件，可以包含函数、类和变量。
# 可以使用 import 语句导入模块，例如：
import math
# 8. 异常处理
# 异常处理用于捕获和处理程序运行时的错误，使用 try、except 语句，例如：
try:
    result = 10 / 0
except ZeroDivisionError:
    print("除以零错误！")
# 9. 文件操作
# Python 提供了多种文件操作方法，包括读取、写入和关闭文件。例如：
with open('example.txt', 'w') as file:
    file.write("Hello, World!")
# 10. 类和对象
# 类是用于创建对象的蓝图，对象是类的实例。类的定义使用 class 关键字，例如：
class Person:
    """表示一个人"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
# 11. 列表推导式
# 列表推导式是一种简洁的创建列表的方法，例如：
squares = [x**2 for x in range(10)]
# 12. 字典推导式
# 字典推导式是一种简洁的创建字典的方法，例如：
squared_dict = {x: x**2 for x in range(10)}
# 13. 集合推导式
# 集合推导式是一种简洁的创建集合的方法，例如：
squared_set = {x**2 for x in range(10)}
# 14. 生成器
# 生成器是一种用于创建迭代器的简单而强大的工具，可以使用 yield 关键字生成值，例如：
def generate_numbers(n):
    """生成从 0 到 n-1 的数字"""
    for i in range(n):
        yield i
# 15. 装饰器
# 装饰器是一种用于修改函数行为的函数，可以使用 @ 符号将装饰器应用于函数，例如：
def decorator(func):
    """装饰器示例"""
    def wrapper(*args, **kwargs):
        print("函数开始执行")
        result = func(*args, **kwargs)
        print("函数执行结束")
        return result
    return wrapper
# 16. 面向对象编程
# 面向对象编程（OOP）是一种编程范式，使用类和对象来组织代码。OOP 的核心概念包括封装、继承和多态。例如：
class Animal:
    """表示一个动物"""
    def speak(self):
        raise NotImplementedError("子类必须实现该方法")
    # 17. 继承
    # 继承是面向对象编程中的一个重要概念，允许一个类继承另一个类的属性和方法。例如：
class Dog(Animal):
    """表示一只狗"""
    def speak(self):
        return "Woof!"
# 18. 多态
# 多态是面向对象编程中的一个重要概念，允许不同类的对象以相同的方式调用方法。例如：
class Cat(Animal):
    """表示一只猫"""
    def speak(self):
        return "Meow!"
    # 19. 模块化编程
# 模块化编程是一种将代码分解为独立模块的编程方法，每个模块可以独立开发、测试和维护。例如：
# 文件：math_utils.py
def add(a, b):
    """返回两个数的和"""
    return a + b
def subtract(a, b):
    """返回两个数的差"""
    return a - b
# 文件：main.py
import math_utils
result1 = math_utils.add(5, 3)
result2 = math_utils.subtract(5, 3)
# 20. 异步编程
# 异步编程是一种允许程序在等待 I/O 操作完成时继续执行其他任务的编程方法。Python 提供了 asyncio 库来支持异步编程。例如：
import asyncio
async def fetch_data():
    """模拟异步获取数据"""
    await asyncio.sleep(1)
    return "数据已获取"
async def main():
    data = await fetch_data()
    print(data)
# 21. 单元测试
# 单元测试是一种用于验证代码功能的测试方法，Python 提供了 unittest 模块来支持单元测试。例如：
import unittest
class TestMathUtils(unittest.TestCase):
    """测试 math_utils 模块"""
    def test_add(self):
        self.assertEqual(math_utils.add(5, 3), 8)
    def test_subtract(self):
        self.assertEqual(math_utils.subtract(5, 3), 2)