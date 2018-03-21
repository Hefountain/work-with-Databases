# -*- coding: utf-8 -*-
# 2018.3.20 by fountain

from alchemy_entity import Base, School
from populate_db import populate

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from pandas.io.sql import read_sql

# create_engine()用来初始化数据库连接。
# SQLAlchemy用一个字符串表示连接信息：'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine =  create_engine('mysql+mysqlconnector://user:password@hostname:port/dbname')

#找到Base下的所有子类，并在数据库中建立这些表
Base.metadata.create_all(engine)

populate(engine)
Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

print "进行读取操作"

# 获取School对象中的第一条数据
print "第一条记录",session.query(School).first()

# 获取所有数据
query = session.query(School)
print "Query 1", query.all()

# 遍历查询
# for scool in query:
# 	print scool.school_name

# 获取id=2那条记录对应的school_name
print query.filter(School.id == 2).first().school_name

# 获取id=1那条记录对应的school_name
print query.get(1).school_name

# 利用pandas中的read_sql函数从数据库中读取数据，对应的是to_sql函数
print read_sql("SELECT * FROM school", engine.raw_connection())


print "进行update操作"
query.filter(School.id==28).update({School.school_name:'Cambridge'})


print "进行删除操作"
# delete
query.filter(School.id.in_((24,25,26))).delete(synchronize_session=False)

session.commit() # 提交

# 利用pandas中的read_sql函数从数据库中读取数据，对应的是to_sql函数
print read_sql("SELECT * FROM school", engine.raw_connection())


session.close()
