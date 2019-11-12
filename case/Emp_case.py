"""
员工模块的增删改查

"""
# 1 导包
import logging
import unittest

import requests

# 2 创建测试类
import app
from api.EmpAPI import EmpCRUD


class Test_EMP(unittest.TestCase):
    # 3初始化函数
    def setUp(self) -> None:
        self.session = requests.Session()
        self.emp_obj = EmpCRUD()

    # 4资源卸载函数
    def tearDown(self) -> None:
        self.session.close()

    # 5 测试函数
    # 直接执行该测试用例失败 原因是什么？
    # 5.1 增
    def test_add(self):
        logging.info('新增员工信息')
        # 请求业务
        response = self.emp_obj.add(self.session, username="lluluil7lu", mobile='178666806672')
        print('员工新增响应结果：', response.json())

        id = response.json().get('data').get('id')
        app.USER_ID = id
        print('新员工的id：', id)

        self.assertEqual(True,response.json().get('success'))
        self.assertEqual(10000, response.json().get('code'))
        self.assertIn('操作成功',response.json().get('message'))

        # 5，3 改

    def test_update(self):
        logging.warning('修改员工信息')
        response = self.emp_obj.update(self.session, app.USER_ID, "lu7vy886")
        print('修改后的响应结果：', response.json())

    # 5.4 查
    def test_get(self):
        logging.info('获取员工信息')
        response = self.emp_obj.get(self.session, app.USER_ID)
        print('修改后查询到的员工信息：', response.json())

    # 5.2 删
    def test_delete(self):
        logging.warning('删除员工信息')
        response = self.emp_obj.delete(self.session, app.USER_ID)
        print('删除成功的响应结果：', response.json())
