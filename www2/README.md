
## sql使用过程
* 存放位置：static/2019.07.02.sql
* 说明：包含了一些sql的功能，如下：
    * -- 根据点击率进行排序
    * -- 根据最近回复时间进行排序，现根据dateandtime列进行排序，如果dateandtime列时间相同，再根据bbsid排序
    * -- 为主表board 和 从表topics创建FK连接
    * -- 删除FK
    * -- 更改FK
    * -- 根据boardid查找boardname/topics，输出dict
    * -- （没有完成）统计帖子的回复数量