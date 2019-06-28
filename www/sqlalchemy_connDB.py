# coding=utf-8
# 导入:
import pickle

from sqlalchemy import Column, String, SmallInteger, Text, DateTime, Integer, BigInteger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


# 定义User对象
class Bbs(Base):
    # 表名
    __tablename__ = 'bbs_bbs'
    # 表结构
    bbsid = Column(SmallInteger(), primary_key=True, autoincrement=True)
    boardid = Column(SmallInteger())
    parentid = Column(SmallInteger())
    child = Column(SmallInteger())
    username = Column(String(100))
    expression = Column(String(100))
    bbstitle = Column(String(200))
    bbscontent = Column(Text())
    dateandtime = Column(DateTime())
    bbsclick = Column(BigInteger())
    bbshot = Column(String(10))


def init():
    try:
        # 初始化数据库连接:
        # '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
        engine = create_engine('mysql+mysqlconnector://root:1234@localhost:3306/bbs_system')
        # 创建DBSession类型:
        DBSession = sessionmaker(bind=engine)
        # 创建session对象: (tips:DBSession为当前数据库连接）
        session = DBSession()
        return session
    finally:
        print('init conn finish')


def insert():
    try:
        session = init()

    finally:
        # 关闭Session:
        session.close()
        print('close session')


def query_one(obj, value):
    session = init()
    try:
        # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
        bbs = session.query(obj).filter(Bbs.bbsid == value).one()
        return convert_to_dict(bbs)
    finally:
        # 关闭Session:
        session.close()
        print('close session')


def update():
    session = init()
    try:
        # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
        # bbs = session.query(Bbs).filter(Bbs.bbsid == None).one()
        bbs = session.update(Bbs)
        return convert_to_dict(bbs)
    finally:
        # 关闭Session:
        session.close()
        print('close session')

def convert_to_dict(obj):
    '''把Object对象转换成Dict对象'''
    dict = {}
    dict.update(obj.__dict__)
    return dict


# def convert_to_dicts(objs):
#     '''把对象列表转换为字典列表'''
#     obj_arr = []
#     for o in objs:
#         # 把Object对象转换成Dict对象
#         dict = {}
#         dict.update(o.__dict__)
#         obj_arr.append(dict)
#
#     return obj_arr
#
#
# def class_to_dict(obj):
#     '''把对象(支持单个对象、list、set)转换成字典'''
#     is_list = obj.__class__ == [].__class__
#     is_set = obj.__class__ == set().__class__
#
#     if is_list or is_set:
#         obj_arr = []
#         for o in obj:
#             #把Object对象转换成Dict对象
#             dict = {}
#             dict.update(o.__dict__)
#             obj_arr.append(dict)
#         return obj_arr
#     else:
#         dict = {}
#         dict.update(obj.__dict__)
#         return dict






