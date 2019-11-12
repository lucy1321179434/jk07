"""
测试需求组合被执行的和函数
"""
#导包
import time
import unittest

import app
from case.Emp_case import Test_EMP
from case.Test_iHRM_Login import Test_Login

# 实例化对象
from tools.HTMLTestRunner import HTMLTestRunner
# 导包
import time
import unittest

import app
from case.Emp_case import Test_EMP
from case.Test_iHRM_Login import Test_Login
# 实例化对象
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(Test_Login('test_login_success')) # 登录成功
suite.addTest(Test_EMP('test_add')) # 新增成功
suite.addTest(Test_EMP('test_update')) # 修改成功
suite.addTest(Test_EMP('test_get')) # 修改后组织查询员工
suite.addTest(Test_EMP('test_delete')) #删除成功后的响应结果

# runner =unittest.TextTestRunner()
# runner.run(suite)

with open(app.PRO_PATH+'/report/'+ time.strftime('%Y%m%d-%H%M%M')+'.html','wb') as f:
    runner =HTMLTestRunner(f,title='人力资源管理系统测试报告', description='测试员工模块增删改查相关接口')
    runner.run(suite)




