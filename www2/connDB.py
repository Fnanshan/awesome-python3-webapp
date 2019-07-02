# coding=utf-8
# 导入MySQL驱动:
import mysql.connector


def init():
    conn = mysql.connector.connect(user='root', password='1234', database='bbs_system')
    cursor = conn.cursor()
    return conn, cursor


def insert(sql):
    try:
        conn, cursor = init()
        # 插入一行记录，注意MySQL的占位符是%s:
        cursor.execute(sql)
        status = cursor.rowcount
        print('insert opt :', status, ' 行受影响！')
        # 提交事务:
        conn.commit()
        return status
    finally:
        cursor.close()
        conn.close()


def delete(sql):
    try:
        conn, cursor = init()
        # 插入一行记录，注意MySQL的占位符是%s:
        cursor.execute(sql)
        status = cursor.rowcount
        print(status, ' 行受影响！')
        # 提交事务:
        conn.commit()
        return status
    finally:
        cursor.close()
        conn.close()


def update(sql):
    try:
        conn, cursor = init()
        # 插入一行记录，注意MySQL的占位符是%s:
        cursor.execute(sql)
        status = cursor.rowcount
        print('update opt :', status, ' 行受影响！')
        # 提交事务:
        conn.commit()
        return status
    except mysql.connector.errors.ProgrammingError as e:
        print('------error :', e)
    except mysql.connector.errors.DataError as e:
        print('------error :', e)
    finally:
        cursor.close()
        conn.close()


def query(sql):
    try:
        conn, cursor = init()
        # 运行查询:
        cursor = conn.cursor()
        cursor.execute(sql)
        values = cursor.fetchall()
        return values
    finally:
        cursor.close()
        conn.close()




