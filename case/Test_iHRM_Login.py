"""
封装 unittest相关实现
"""
# 1导包
import json
import unittest

import requests
from parameterized import parameterized

import app
from api.LoginAPI import Login


# 参数化解析


def read_json_file():
    # 创建空列表
    data = []
    # 解析文件流 添加数据至列表
    with open(app.PRO_PATH + '/data/login_data.json', 'r', encoding='utf-8') as f:
        for v in json.load(f).values():
            mobile = v.get('mobile')
            password = v.get('password')
            success = v.get('success')
            code = v.get('code')
            message = v.get('message')
            ele = (mobile, password, success, code, message)
            data.append(ele)
    # 返回列表
    return data


# 2创建测试类
class Test_Login(unittest.TestCase):
    # 3 初始化函数
    def setUp(self) -> None:
        # 初始化session
        self.session = requests.session()
        # 初始化api对象
        self.login_obj = Login()

    # 4 资源卸载函数
    def tearDown(self) -> None:
        self.session.close()  # 销毁session

    # 5 核心 —— 测试函数 -登录
    # 5-1 参数化
    @parameterized.expand(read_json_file())
    def test_login(self, mobile, password, success, code, message):
        print('-' * 100)
        print('参数化读取的数据：', mobile, password, success, code, message)
        # 5-2 请求业务
        response = self.login_obj.login(self.session, mobile, password)
        print('登录数据', response.json())
        # 5-3 断言业务

        self.assertEqual(success, response.json().get('success'))
        self.assertEqual(code, response.json().get('code'))
        self.assertIn(message, response.json().get('message'))

    # 编写登录成功的测试函数
    def test_login_success(self):
        # 1 直接通过提交正向的数据发送请求
        response = self.login_obj.login(self.session, '13800000002', '123456')
        # 断言业务
        print('登录成功的结果：', response.json())
        self.assertEqual(True, response.json().get('success'))
        self.assertEqual(10000, response.json().get('code'))
        self.assertIn('操作成功', response.json().get('message'))
        # 提取 token
        token = response.json().get('data')
        print('登录后的token：', token)
        # 预期允许其他文件调用该token值，可以扩大token的作用域（将token赋值给 app.py的一个全局变量）
        app.TOKEN = token
