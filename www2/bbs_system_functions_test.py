# coding=utf-8
import bbs_system_functions as system

print('------board opt------')
board = system.Board()
request = 1
# result = board.get_boardid_dict()
# for i in result:
#     if i[0] == request:
#         print(i[1])
# result = board.get_board_id_and_name()
# for i in result:
#     if i[0] == request:
#         print(i[1])


print('------bbs opt------')
bbs = system.Bbs()
# bbs.bbsid = 1
# bbs.boardid = 1
# bbs.parentid = 0
# bbs.child = 0
# bbs.username = 'admin'
# bbs.expression = '@qq.com'
# bbs.bbstitle = '【贴吧辩论赛】高温天气，宿舍该不该开空调？'
# bbs.bbscontent = ''
# bbs.dateandtime = '2000-01-01 00:00:00'
# bbs.bbsclick = 0
# bbs.bbshot = ''

# result = bbs.clicking_ranking()
# for i in result:
#     print(i, '\n')

# result = bbs.order_by_dateandtime()
# for i in result:
#     print(i, '\n')

# result = bbs.bbs_sum_reply()
# sum = 0
#
# for i in result:
#     sum += i[0]
# print(sum)

# bbs.bbsid = 1
# print(bbs.query_by_bbsid())

print('------user opt------')