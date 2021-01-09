# coding=UTF-8

from redis import *

if __name__ == "__main__":
	try:
		sr = StrictRedis() # 创建与redis数据库的连接

	except Exception as e:
		print(e)

	else:
		sr.set('string','这是个string')
		print(sr.get('string'))
		res = sr.delete('string')# 返回值是删除了几个
		print(res)
		print(sr.keys())
		print("嬲你妈妈别")