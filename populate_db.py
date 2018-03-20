# -*- coding: utf-8 -*-
# 2018.3.20 by fountain

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from alchemy_entity import Base, User

def populate(engine):
	
	Base.metadata.bind = engine
	
	# 创建DBSession类型
	DBSession = sessionmaker(bind=engine)
	
	# 创建session对象
	session = DBSession()
	user_info = User(name='xiaoming')

	# 添加到session
	session.add(user_info)
	session.commit()

	print "User", user_info

if __name__ == "__main__":
	print "This (populate_db)script is used by another script"
