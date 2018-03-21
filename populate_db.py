# -*- coding: utf-8 -*-
# 2018.3.20 by fountain

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from alchemy_entity import Base, School

# 解决中文问题：
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 10-11: ordinal not in range(128)
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


def populate(engine):	
	Base.metadata.bind = engine
	
	# 创建DBSession类型，即数据库会话类
	DBSession = sessionmaker(bind=engine)
	
	# 创建session对象，有了session，就可以用它去执行SQL了
	session = DBSession()
	school_info = School(school_name='清华')

	# 添加到session
	session.add(school_info)
	session.commit()

	print "School", school_info

if __name__ == "__main__":
	print "This (populate_db)script is used by another script"
