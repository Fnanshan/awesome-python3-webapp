# 项目简介
* 本项目是基于flask开发的BBS论坛
* 作者：[Fnanshan](https://github.com/Fnanshan)
* 开发环境：
    * Python 3.7.3
    * conda 4.6.14
        * web env (参考conf目录:web_environment.yaml)
    * flask 1.0.3
    * Werkzeug 0.15.4
    * 5.7.17 MySQL Community Server (GPL)
    * Pycharm 2019.1.2
    * Bootstrap3、JS、JQuery
* 功能描述：
    * 用户管理
    * 板块管理
* 结构简介  
    * /conf/：程序配置目录
        * 2019-07-02.sql：7月2日对sql的操作
        * bbs_system.sql：数据库、表文件
        * web_environment.yaml：conda环境文件
    * /www/：最初版本代码
    * /www2/：最终版本代码
        * app.py：代码启动项
        * bbs_system_function.py：对系统的模块化开发，应用面向对象思想，如Bbs()/Board()/User()类
        * connDB.py：对sql操作的封装，如init()/delete()/insert()/query()/update()
        * (temp) opt_functions.py：暂时没用的代码
        * /static/：静态文件目录，内含bootstrap、jQuery、JS
        * /templates/：前端模板目录
    * /学习/：学习过程中的一些样例代码，可参考使用
