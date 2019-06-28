# import logging;
import logging
from logging import log

import aiomysql as aiomysql

logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web, web_runner


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/layui_html')

# # 存在弃用警告，重写代码
# @asyncio.coroutine
# def init(loop):
#     # 弃用警告-DeprecationWarning: loop argument is deprecated
#     app = web.Application(loop=loop)
#     app.router.add_route('GET', '/', index)
#     # 弃用警告-DeprecationWarning: Application.make_handler(...) is deprecated, use AppRunner API instead
#     srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
#     logging.info('server started at http://127.0.0.1:9000...')
#     return srv
#
#
# loop = asyncio.get_event_loop()
# # run_until_complete() : Run the event loop until a Future is done.
# #                        Return the Future's result, or raise its exception.
# loop.run_until_complete(init(loop))
# # run_forever() : Run the event loop until stop() is called
# loop.run_forever()

@asyncio.coroutine
def init():
    app = web.Application()
    app = web_runner.AppRunner(app=app).app()
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app._make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init())
loop.run_forever()


'''
1. app = web.Application(loop=loop)
2. 由于Web框架使用了基于asyncio的aiohttp，这是基于协程的异步模型。在协程中，不能调用普通的同步IO操作
3. 异步编程的一个原则：一旦决定使用异步，则系统每一层都必须是异步。
4. 创建全局的连接池，每个HTTP请求都可以从连接池中直接获取数据库连接。
5. 连接池由全局变量__pool存储，缺省情况下将编码设置为utf8，自动提交事务

'''
@asyncio.coroutine
def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = yield from aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf-8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )


@asyncio.coroutine
def select(sql, args, size=None):
    log(sql, args)
    global __pool
    with (yield from __pool) as conn:
        cur = yield from conn.cursor(aiomysql.DictCursor)
        yield from cur.execute(sql.replace('?', '%s'), args or ())
        if size:
            rs = yield from cur.fetchmany(size)
        else:
            rs = yield from cur.fetchall()
        yield from cur.close()
        logging.info('rows returned: %s' % len(rs))
        return rs


@asyncio.coroutine
def execute(sql, args):
    log(sql)
    with (yield from __pool) as conn:
        try:
            cur = yield from conn.cursor()
            yield from cur.execute(sql.replace('?', '%s'), args)
            affected = cur.rowcount
            yield from cur.close()
        except BaseException as e:
            raise
        return affected


# 有了基本的select()/execute()，可以编写一个简单的ORM

# 定义一个User对象，把table中的users和它关联起来
# 需要在orm的__init__.py中定义Model/StringField/IntegerField
# from orm import Model, StringField, IntegerField
from orm import Model, StringField, IntegerField


class User(Model):
    __table__ = 'users'

    id = IntegerField(primary_key=True)
    name = StringField()


def main():
    # 创建实例
    user = User(id=123, name='Michael')
    # 存入数据库
    yield from user.save()
    # # 查询所有的User对象
    # users = User.findAll()
    # # 通过类方法实现主键查找
    # user = yield from User.find('123')


main()
