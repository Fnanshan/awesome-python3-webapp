/*
Navicat MySQL Data Transfer

Source Server         : test
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : bbs_system

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2019-07-09 14:36:13
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for bbs_bbs
-- ----------------------------
DROP TABLE IF EXISTS `bbs_bbs`;
CREATE TABLE `bbs_bbs` (
  `bbsid` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '帖子自动编号',
  `boardid` bigint(20) DEFAULT NULL COMMENT '板块编号',
  `parentid` bigint(20) DEFAULT NULL COMMENT '父帖编号',
  `child` bigint(20) DEFAULT NULL COMMENT '跟帖数',
  `username` varchar(100) DEFAULT NULL COMMENT '发表人姓名',
  `expression` varchar(100) DEFAULT NULL COMMENT '发帖人E-mail',
  `bbstitle` varchar(200) DEFAULT NULL COMMENT '发表人标题',
  `bbscontent` text COMMENT '文章内容',
  `dateandtime` datetime DEFAULT NULL COMMENT '文章发表时间',
  `bbsclick` bigint(20) DEFAULT NULL COMMENT '论坛点击率',
  `bbshot` varchar(10) CHARACTER SET utf8mb4 DEFAULT NULL COMMENT '是否为精华帖',
  PRIMARY KEY (`bbsid`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of bbs_bbs
-- ----------------------------
INSERT INTO `bbs_bbs` VALUES ('1', '1', '0', '2', 'admin', '@qq.com', 'How do I avoid typing “git” at the begining of every Git command?', '\r\n\r\nI\'m wondering if there\'s a way to avoid having to type the word git at the beginning of every Git command.\r\n\r\nIt would be nice if there was a way to use the git command only once in the beginning after opening a command prompt to get into \"Git mode\".\r\n\r\nFor example:\r\n\r\ngit>\r\n\r\nAfter which every command we type is by default interpreted as a Git command.\r\n\r\nIn a way similar to how we use the MySQL shell to write database commands:\r\n\r\nmysql>\r\n\r\nThis will save me from typing \'git\' hundreds of time every day.\r\n\r\nNOTE: I\'m using git-bash, on Windows.\r\n', '2019-06-24 14:17:00', '0', '1');
INSERT INTO `bbs_bbs` VALUES ('2', '1', '1', '1', 'PDD吧务君', 'test@qq.com', null, 'To those who have voted to close on the basis of it being off-topic, please read the text you are clicking on: \"Questions about general computing hardware and software are off-topic for Stack Overflow unless they directly involve tools used primarily for programming.\". Git is a tool used by programmers. As evidenced by the fact that it has its own tag on this site.', '2019-06-24 14:18:00', '1', '0');
INSERT INTO `bbs_bbs` VALUES ('3', '1', '1', '0', 'PDD吧务君', 'test@qq.com', null, 'Why are you typing \"git\" so much? Your IDE should have powerful vcs integrations available at a keypress. Do you rather type \"git pull\" 50 times a day, or ctrl-t... stop being a command line warrior when you dont need to be ;)', '2019-06-24 14:27:00', '3', '0');
INSERT INTO `bbs_bbs` VALUES ('4', '1', '2', '0', '我有半卷书', 'test@qq.com', null, 'Practically all git help and wisdom is given in terms of command-line.', '2019-06-24 16:53:00', '1', '0');
INSERT INTO `bbs_bbs` VALUES ('5', '2', '0', '1', '天降正义', 'test@qq.com', 'Most elegant way to write a one-shot \'if\'', '\r\n\r\nSince C++ 17 one can write an if block that will get executed exactly once like this:\r\n\r\n#include <iostream>\r\nint main() {\r\n    for (unsigned i = 0; i < 10; ++i) {\r\n\r\n        if (static bool do_once = true; do_once) { // Enter only once\r\n            std::cout << \"hello one-shot\" << std::endl;\r\n            // Possibly much more code\r\n            do_once = false;\r\n        }\r\n\r\n    }\r\n}\r\n\r\nI know I might be overthinking this, and there are other ways to solve this, but still - is it possible to write this somehow like this, so there is no need of the do_once = false at the end?\r\n\r\nif (DO_ONCE) {\r\n    // Do stuff\r\n}\r\n\r\nI\'m thinking a helper function, do_once(), containing the static bool do_once, but what if I wanted to use that same function in different places? Might this be the time and place for a #define? I hope not.\r\n', '2019-06-25 17:33:00', '10', '1');
INSERT INTO `bbs_bbs` VALUES ('8', '2', '5', '1', '石不能言', 'test@qq.com', null, 'Why not just if (i == 0)? It\'s clear enough', '2019-06-25 17:35:00', '1', '0');
INSERT INTO `bbs_bbs` VALUES ('9', '2', '5', '0', '贴吧用户_58AKS5W\r\n', 'est@qq.com', null, '把库里放到过去，场均200个三分。反正没有的事，怎么爽怎么说\r\nmaybe std::call_once is an option (it\'s used for threading, but still does it\'s job).', '2019-06-25 17:36:00', '1', '0');
INSERT INTO `bbs_bbs` VALUES ('10', '2', '8', '0', '哩甲塞', 'test@qq.com', null, 'Because that is not the point. This if-block might be somewhere in some function that gets executed multiple times, not in a regular loop', '2019-06-26 22:21:00', '1', '0');

-- ----------------------------
-- Table structure for bbs_user
-- ----------------------------
DROP TABLE IF EXISTS `bbs_user`;
CREATE TABLE `bbs_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '会员编号',
  `username` varchar(100) DEFAULT NULL COMMENT '会员姓名',
  `userpass` varchar(100) DEFAULT NULL COMMENT '会员密码',
  `usertype` int(10) DEFAULT '2' COMMENT '用户类型：0 管理员；1游客；2普通用户',
  `usermail` varchar(100) DEFAULT NULL COMMENT '会员E-mail',
  `userhomepage` varchar(200) DEFAULT NULL COMMENT '会员主页',
  `homepagename` varchar(200) DEFAULT NULL COMMENT '会员主页名称',
  `sex` varchar(10) DEFAULT NULL COMMENT '会员性别',
  `comefrom` varchar(100) DEFAULT NULL COMMENT '会员籍贯',
  `usersign` varchar(100) DEFAULT NULL COMMENT '会员格言',
  `redate` datetime DEFAULT NULL COMMENT '会员注册时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10004 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of bbs_user
-- ----------------------------
INSERT INTO `bbs_user` VALUES ('1', 'admin', 'admin', '0', null, null, null, null, null, null, null);
INSERT INTO `bbs_user` VALUES ('2', 'daemon', 'daemon', '0', null, null, null, null, null, null, null);
INSERT INTO `bbs_user` VALUES ('3', 'update', 'update', '0', null, null, null, null, null, null, null);
INSERT INTO `bbs_user` VALUES ('4', 'mymy', 'mymy', '0', null, null, null, null, null, null, null);
INSERT INTO `bbs_user` VALUES ('14', '5', '5', '2', null, null, null, null, null, null, null);
INSERT INTO `bbs_user` VALUES ('20', 'guest', 'guest', '2', 'test@qq.com', null, null, '1', null, null, '2019-07-02 17:14:00');
INSERT INTO `bbs_user` VALUES ('21', '1', '1', '2', null, null, null, null, null, null, null);
INSERT INTO `bbs_user` VALUES ('10000', '10000', '10000', '0', 'test@qq.com', 'test', 'test', '1', 'test', 'test', '2019-07-06 17:14:00');
INSERT INTO `bbs_user` VALUES ('10001', '10001', '10001', '2', 'test@qq.com', 'test', 'test', '0', 'test', 'test', '2019-07-06 17:14:00');
INSERT INTO `bbs_user` VALUES ('10003', '10002', '10002', '2', null, null, null, null, null, null, null);

-- ----------------------------
-- Table structure for board
-- ----------------------------
DROP TABLE IF EXISTS `board`;
CREATE TABLE `board` (
  `boardid` int(11) NOT NULL AUTO_INCREMENT COMMENT '板块自动编号',
  `boardname` varchar(200) NOT NULL COMMENT '版块名称',
  `boardtopics` int(11) DEFAULT '0' COMMENT '版块主题数',
  `boardmanager` varchar(100) NOT NULL COMMENT '版主名',
  `boardintroduce` varchar(500) DEFAULT '' COMMENT '板块介绍',
  PRIMARY KEY (`boardid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of board
-- ----------------------------
INSERT INTO `board` VALUES ('1', 'defalut', '1', 'admin', 'this is defalut board');
INSERT INTO `board` VALUES ('2', 'shoot', '2', 'admin', 'this is display shoot board');
INSERT INTO `board` VALUES ('3', 'tech', '2', 'guest', 'this is display tech board');
INSERT INTO `board` VALUES ('4', 'test', '0', 'guest', 'test');
INSERT INTO `board` VALUES ('5', 'test', '0', 'test', 'test');
INSERT INTO `board` VALUES ('6', '', '0', 'sssss', '');
INSERT INTO `board` VALUES ('7', 'test', '0', 'admin', 'test\r\n');
INSERT INTO `board` VALUES ('8', 'test', '0', 'admin', 'test\r\n');
INSERT INTO `board` VALUES ('9', 'test', '0', 'admin', 'test');

-- ----------------------------
-- Table structure for topics
-- ----------------------------
DROP TABLE IF EXISTS `topics`;
CREATE TABLE `topics` (
  `topicsid` int(11) NOT NULL AUTO_INCREMENT COMMENT '主题id',
  `boardid` int(11) NOT NULL COMMENT '所属板块id',
  `topics_name` varchar(200) NOT NULL COMMENT '主题名称',
  `topics_manager` varchar(100) DEFAULT NULL COMMENT '主题管理者',
  `remarks` varchar(255) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`topicsid`),
  KEY `fk_topics_board` (`boardid`),
  CONSTRAINT `fk_topics_board` FOREIGN KEY (`boardid`) REFERENCES `board` (`boardid`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of topics
-- ----------------------------
INSERT INTO `topics` VALUES ('1', '1', 'test_default', 'admin', null);
INSERT INTO `topics` VALUES ('2', '2', 'portrait', 'admin', null);
INSERT INTO `topics` VALUES ('3', '2', 'scenery', 'admin', null);
INSERT INTO `topics` VALUES ('4', '3', 'computer', 'daemon', null);
INSERT INTO `topics` VALUES ('5', '3', 'deepin learning', 'daemon', null);
