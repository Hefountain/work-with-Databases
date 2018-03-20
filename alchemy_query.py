# -*- coding: utf-8 -*-
# 2018.3.20 by fountain

from alchemy_entity import Base, User
from populate_db import populate

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from pandas.io.sql import read_sql

# 初始化数据库连接
engine =  create_engine('mysql+mysqlconnector://user:password@hostname:port/dbname')
Base.metadata.create_all(engine)
populate(engine)
Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

# 获取User对象中的第一条数据
# user = session.query(User).first()

# 获取所有数据
print "Query 1", session.query(User).all()

# 利用pandas中的read_sql函数从数据库中读取数据，对应的是to_sql函数
print read_sql("SELECT * FROM user", engine.raw_connection())

session.close()
