# -*- coding: utf-8 -*-

##TODO 定时备份数据库脚本同时发邮件

exec("cd /home/fpx/bluelog && sqlite3 blogfei-dev.db .dump > /tmp/blogfei.sql")