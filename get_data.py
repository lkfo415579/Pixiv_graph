#coding:utf-8
import uniout
import MySQLdb

host = "127.0.0.1"
global db
global dbc
db = MySQLdb.connect(host=host, user='lkfo', passwd='qq321520', db='pixiv')
db.set_character_set('utf8')
dbc= db.cursor()
dbc.execute('SET NAMES utf8;')
dbc.execute('SET CHARACTER SET utf8;')
dbc.execute('SET character_set_connection=utf8;')


def Title_Tags():
	sys_sql = "select title,tags from pictures"
	print (sys_sql)
	dbc.execute(sys_sql)
	result = dbc.fetchall()
	dbc.close()
	return result
	
print Title_Tags()[:5]