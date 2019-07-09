select * from board

select * from topics

-- 根据点击率进行排序
-- select bbstitle, bbsclick from bbs_bbs
-- where bbstitle is not null
-- ORDER BY bbsclick desc

-- 根据最近回复时间进行排序，现根据dateandtime列进行排序，如果dateandtime列时间相同，再根据bbsid排序
select * from bbs_bbs
where bbstitle is not null
ORDER BY dateandtime DESC, bbsid DESC

-- 为主表board 和 从表topics创建外键连接
ALTER TABLE `topics`
ADD CONSTRAINT `fk_topics_board` FOREIGN KEY (`boardid`) REFERENCES `board` (`boardid`);

-- crud操作进行验证
select * from board
select * from topics

-- 删除主表board中数据：delete FROM `board` WHERE id=1，会报错：
DELETE FROM 'board' 
WHERE boardid = 1;
-- 从表topics中，添加不存在的 boardid：insert into topics(boardid,topics_name) values(4, 'test') 会报错
insert into topics(boardid,topics_name) values(4, 'test');

-- 删除外键
ALTER TABLE topics DROP FOREIGN KEY fk_topics_board

-- 更改FK
ALTER TABLE `topics` ADD CONSTRAINT `fk_topics_board` FOREIGN KEY ( `boardid` )
REFERENCES `board` ( `boardid` )
ON UPDATE CASCADE

-- 根据boardid查找boardname/topics，输出dict
select boardid, boardname from board
select boardid, topics_name from topics

select * 
from board left JOIN topics on board.boardid = topics.boardid

select a.boardid, a.boardname, b.topics_name
from (select boardid, boardname from board) as a INNER JOIN (select boardid, topics_name from topics) as b
ON a.boardid=b.boardid


-- （没有完成）统计帖子的回复数量
select * from bbs_bbs

-- 1 获得每个帖子的bbsid, bbstitle，输出(1, 5)
select bbsid, bbstitle from bbs_bbs
where bbstitle is not NULL

-- 2. 根据bbsid统计每个帖子下的回复数量
-- 2.1 获得每个帖子的直接回复，输出(2, 3, 8, 9)
select *									
from bbs_bbs
where parentid in (1, 5)

-- 2.2 获得每个帖子的间接回复，输出(4, 10)
select *
from bbs_bbs
where parentid in (2, 3, 8, 9)

select *
from bbs_bbs
where parentid in (
	select bbsid									
	from bbs_bbs
	where parentid in (
		select bbsid from bbs_bbs
		where bbstitle is not NULL
	)
)

-- 2.3 知道(2, 3, 8, 9) 和 (4, 10) 是帖子回复数，怎么能分别知道每个帖子的回复数？
