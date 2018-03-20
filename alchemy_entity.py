# -*- coding: utf-8 -*-
# 2018.3.20 by fountain

from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base

# ORM技术：Object-Relational Mapping，把关系数据库的表结构映射到对象上
# 而SQLAlchemy正是最有名的ORM框架


# 创建对象的基类
Base = declarative_base()

# 定义User对象

class User(Base):
	# 表的名字
	__tablename__ = 'user'

	# 表的结构
	id = Column(Integer, primary_key=True)
	name = Column(String(20), nullable=False)

	def __repr__(self):
		return "Id=%d name=%s" %(self.id, self.name)

if __name__ == "__main__":
	print "This (alchemy_entity)script is used by another script"