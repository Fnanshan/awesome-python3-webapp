# coding=utf-8
from typing import Iterable
import connDB
# this is www2 code

def login(username, userpass):
    '''
    flag=0  not find user
    flag=1  userpass error
    flag=2  valid success
    '''
    sql = 'select username, userpass from bbs_user where username= \'' + username + '\''
    sql_return = connDB.query(sql)
    # 如果存在用户
    if len(sql_return) > 0:
        if username == sql_return[0][0] and userpass == sql_return[0][1]:
            # 如果用户名、用户密码正确
            return 2
        # 如果用户名or密码不正确
        return 1
    # 如果不存在用户
    return 0


def register(username, userpass):
    '''
    flag=1   可以注册
    flag=0   不可以注册
    '''
    # * 判断数据库中是否有相同的username
    query_sql = 'select username from bbs_user where username= \'' + username + '\''
    sql_return = connDB.query(query_sql)

    # 如果数据库中有要注册的username，返回错误信息
    if sql_return:
        return 0
    # 插入数据
    insert_sql = 'insert into bbs_user (username, userpass) values (\'' + username + '\', \'' + userpass + '\')'
    connDB.insert(insert_sql)
    return 1


class Board(object):

    @property
    def boardid(self):
        return self.__boardid

    @boardid.setter
    def boardid(self, boardid):
        self.__boardid = boardid

    @property
    def boardname(self):
        return self.__boardname

    @boardname.setter
    def boardname(self, boardname):
        self.__boardname = boardname

    @property
    def boardtopics(self):
        return self.__boardtopics

    @boardtopics.setter
    def boardtopics(self, boardtopics):
        self.__boardtopics = boardtopics

    @property
    def boardmanager(self):
        return self.__boardmanager

    @boardmanager.setter
    def boardmanager(self, boardmanager):
        self.__boardmanager = boardmanager

    @property
    def boardintroduce(self):
        return self.__boardintroduce

    @boardintroduce.setter
    def boardintroduce(self, boardintroduce):
        self.__boardintroduce = boardintroduce

    def query_board(self):
        query_board_sql = 'select * from board;'
        result = connDB.query(query_board_sql)
        return result

    def insert_board(self):
        # 添加版块时，标题与内容不能为空，否则弹出错误提示。
        # sql = 'insert into board （boardname, boardtopics, boardmanager, boardintroduce) values (\'' + self.__boardname + '\', ' + str(self.__boardtopics) + ', \'' + self.__boardmanager + '\', \'' + self.__boardintroduce + '\');'
        sql = 'insert into board (boardname, boardtopics, boardmanager, boardintroduce) VALUES \
( \'' + self.__boardname + '\', ' + str(self.__boardtopics) + ', \'' + self.__boardmanager + '\', \'' + self.__boardintroduce + '\')'
        status = connDB.insert(sql)
        return status

    def update_board(self):
        '''
        UPDATE table_name SET field1=new-value1, field2=new-value2
            [WHERE Clause]
            '''
        sql = 'update board set boardname=\'' + self.__boardname + '\', boardtopics=' + str(self.__boardtopics) + ', boardmanager=\'' + self.__boardmanager + '\', boardintroduce=\'' + self.__boardintroduce + '\' where boardid=' + str(self.__boardid) + ';'
        status = connDB.update(sql)
        return status

    def delete_board(self):
        '''DELETE FROM table_name [WHERE Clause]'''
        sql = 'delete from board where boardid=' + str(self.__boardid) + ';'
        status = connDB.delete(sql)
        return status

    def get_boardid_dict(self):
        sql = 'select a.boardid, a.boardname, b.topics_name \
                from (select boardid, boardname from board) as a INNER JOIN (select boardid, topics_name from topics) as b ON a.boardid = b.boardid'
        result = connDB.query(sql)
        print(result)
        return result

    def get_board_id_and_name(self):
        sql = 'select boardid, boardname from board'
        result = connDB.query(sql)
        print(result)
        return result


class User(object):

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def userpass(self):
        return self.__userpass

    @userpass.setter
    def userpass(self, userpass):
        self.__userpass = userpass

    @property
    def usertype(self):
        return self.__usertype

    @usertype.setter
    def usertype(self, usertype):
        self.__usertype = usertype

    @property
    def usermail(self):
        return self.__usermail

    @usermail.setter
    def usermail(self, usermail):
        self.__usermail = usermail

    @property
    def userhomepage(self):
        return self.__userhomepage

    @userhomepage.setter
    def userhomepage(self, userhomepage):
        self.__userhomepage = userhomepage

    @property
    def homepagename(self):
        return self.__homepagename

    @homepagename.setter
    def homepagename(self, homepagename):
        self.__homepagename = homepagename

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex):
        self.__sex = sex

    @property
    def comefrom(self):
        return self.__comefrom

    @comefrom.setter
    def comefrom(self, comefrom):
        self.__comefrom = comefrom

    @property
    def usersign(self):
        return self.__usersign

    @usersign.setter
    def usersign(self, usersign):
        self.__usersign = usersign

    @property
    def redate(self):
        return self.__redate

    @redate.setter
    def redate(self, redate):
        self.__redate = redate

    def insert(self):
        # INSERT INTO table_name ( field1, field2,...fieldN )
        #                        VALUES
        #                        ( value1, value2,...valueN );
        sql = 'insert into bbs_user (username, userpass) values (\'' + self.__username + '\', \'' + self.__userpass + '\')'
        status = connDB.insert(sql)
        return status

    def delete(self):
        # DELETE FROM table_name [WHERE Clause]
        sql = 'delete from bbs_user where id = ' + str(self.__id) + ';'
        print(sql)
        status = connDB.delete(sql)
        return status

    def update(self):
        # UPDATE table_name SET field1=new-value1, field2=new-value2
        # [WHERE Clause]
        # usermail=NULL, userhomepage=NULL, homepagename=NULL, sex=NULL, comefrom=NULL, usersign=NULL, redate=NULL
        sql = 'update bbs_user set username=\'' + self.__username + '\', userpass=\'' + self.__userpass + '\' where id=' + str(self.__id) + ';'
        status = connDB.update(sql)
        return status

    def query_all_by_id(self):
        sql = 'select * from bbs_user where id = ' + str(self.__id) + ';'
        result = connDB.query(sql)
        return result

    def query_all_by_username(self):
        sql = 'select * from bbs_user where username = \'' + self.__username + '\';'
        result = connDB.query(sql)
        return result

    def query_all_user(self):
        sql = 'select * from bbs_user'
        result = connDB.query(sql)
        return result


class Bbs(object):

    @property
    def bbsid(self):
        return self.__bbsid

    @bbsid.setter
    def bbsid(self, bbsid):
        self.__bbsid = bbsid

    @property
    def boardid(self):
        return self.__boardid

    @boardid.setter
    def boardid(self, boardid):
        self.__boardid = boardid

    @property
    def parentid(self):
        return self.__parentid

    @ parentid.setter
    def parentid (self, parentid):
        self.__parentid = parentid

    @property
    def child(self):
        return self.__child

    @child.setter
    def child (self, child):
        self.__child = child

    @property
    def username(self):
        return self.__username

    @username.setter
    def username (self, username):
        self.__username = username

    @property
    def expression(self):
        return self.__expression

    @expression.setter
    def expression (self, expression):
        self.__expression = expression

    @property
    def bbstitle(self):
        return self.__bbstitle

    @bbstitle.setter
    def bbstitle (self, bbstitle):
        self.__bbstitle = bbstitle

    @property
    def bbscontent(self):
        return self.__bbscontent

    @bbscontent.setter
    def bbscontent (self, bbscontent):
        self.__bbscontent = bbscontent

    @property
    def dateandtime(self):
        return self.__dateandtime

    @dateandtime.setter
    def dateandtime(self, dateandtime):
        self.__dateandtime = dateandtime

    @property
    def bbsclick(self):
        return self.__bbsclick

    @ bbsclick.setter
    def bbsclick (self, bbsclick):
        self.__bbsclick = bbsclick

    @property
    def bbshot(self):
        return self.__bbshot

    @ bbshot.setter
    def bbshot (self, bbshot):
        self.__bbshot = bbshot

    def inset(self):
            sql = 'insert into bbs_bbs (boardid, parentid, child, username, expression, bbstitle, bbscontent, dateandtime, bbsclick, bbshot) values (' + str(self.__boardid) + ', ' + str(self.__parentid) + ', '  + str(self.__parentid) +  ', \'' + self.username + '\', \'' + self.__expression + '\',\' ' + self.__bbstitle + '\', \'' + self.bbscontent + '\', \'' + self.__dateandtime + '\', \'' + self.bbsclick + '\', \'' + self.bbshot + '\');'
            status = connDB.insert(sql)
            return status

    def delete(self):
        # DELETE FROM table_name [WHERE Clause]
        sql = 'delete from bbs_bbs where bbsid = ' + str(self.__bbsid) + ';'
        # status = connDB.delete(sql)
        # return status
        print(sql)

    def update(self):
        # UPDATE table_name SET field1=new-value1, field2=new-value2
        # [WHERE Clause]
        sql = 'update bbs_bbs set boardid=' + str(self.__boardid) + ', parentid=' + str(self.__parentid) + ', child=' + str(self.__child) + ', username=\'' + str(self.__username) + '\', expression=\'' + self.__expression + '\', bbstitle=\'' + self.__bbstitle + '\', bbscontent=\'' + self.__bbscontent + '\', dateandtime=\'' + str(self.__dateandtime) + '\', bbsclick=' + str(self.bbsclick) + ', bbshot=\'' + self.bbshot + '\' where bbsid=' + str(self.__bbsid) + ';'
        status = connDB.update(sql)
        return status

    def query_all_bbs(self):
        sql = 'select * from bbs_bbs where bbstitle is not null; '
        result = connDB.query(sql)
        return result

    def query_by_bbsid(self):
        sql = 'select * from bbs_bbs where bbsid = ' + str(self.__bbsid) + ';'
        result = connDB.query(sql)
        return result

    # 计算帖子的总回复数，直接回复、间接回复
    def bbs_sum_reply(self):
        sql = '	select count(1) from bbs_bbs where parentid in ( \
                    select bbsid from bbs_bbs where parentid in ( \
                        select bbsid from bbs_bbs where bbsid = ' + str(self.__bbsid) + ') \
                ) \
                UNION  ALL \
                    select count(1) from bbs_bbs where parentid in ( \
                        select bbsid from bbs_bbs where bbsid = ' + str(self.__bbsid) + ')'
        result = connDB.query(sql)
        return result

    def clicking_ranking(self):
        sql = 'select * from bbs_bbs \
                where bbstitle is not null \
                ORDER BY bbsclick desc'
        result = connDB.query(sql)
        return result

    def order_by_dateandtime(self):
        sql = 'select * from bbs_bbs \
                where bbstitle is not null \
                ORDER BY dateandtime DESC, bbsid DESC'
        result = connDB.query(sql)
        return result