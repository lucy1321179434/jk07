"""
app.py 封装数据
"""
import logging
import logging.handlers
import os
# 封装接口的URL前缀
import time

BASE_URL = 'http://182.92.81.159'

# 封装项目路径
FILE_PATH = os.path.abspath(__file__)
PRO_PATH = os.path.dirname(FILE_PATH)
print('动态获取项目绝对路径：', PRO_PATH)


# 获取路径简化代码
# PRO_PATH=os.path.dirname(os.path.abspath(__file__))

# 定义一个全局变量
TOKEN = None
USER_ID = None

# 配置日志模块
def my_log_config():
    #1 获取日志对象
    logger=logging.getLogger()
    # 2 配置日志级别
    logger.setLevel(logging.INFO)
    # 3 配置输出目标
    to_1 =logging.StreamHandler()
    to_2 = logging.handlers.TimedRotatingFileHandler(PRO_PATH+'/log/'+ time.strftime("%Y%m%d-%H%M%M"),
                                                     when='h',
                                                     interval=12,
                                                     backupCount=10,
                                                     encoding='utf-8')
    # 4 配置输出格式
    formatter =logging.Formatter('%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s')
    # 5 组织配置并添加进日志对象
    to_1.setFormatter(formatter)
    to_2.setFormatter(formatter)
    logger.addHandler(to_1)
    logger.addHandler(to_2)

# # 调用
# my_log_config()
# print(logging.info('hello'))
# print(logging.warning('危险'))
