import sqlite3

# 创建数据库在内存中
with sqlite3.connect(":memory:") as con:
	# 定义一个游标
	c = con.cursor()
	# execute()--执行sql语句
	c.execute('''create table sensors
		         (date text, city text, sensor_id real, 
		     temperature real)''')

	for table in c.execute("select name from sqlite_master where type='table'"):
		print "Table", table[0]

	c.execute("insert into sensors values('2018-3-20','NewYork',42,12.5)")
	c.execute("select * from sensors")

	# fetchone从结果中取一条记录
	print c.fetchone()
	con.execute("drop table sensors")

	print "# of tables", c.execute("select count(*) from sqlite_master where type='table'").fetchone()[0]
	c.close()

