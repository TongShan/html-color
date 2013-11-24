#!/usr/bin/python
#coding:utf8

class Milo():
	name = "test"

	def fun1(self):
		print self.name
		print "我是公有方法"
		self.__fun2()

	def __fun2(self):
		print self.name
		print "我是私有方法"

	@classmethod  #装饰器，转换下面函数为类方法
	def classFun(self):
		print self.name
		print "我是类方法"

    # classNewFun = classmethod(classFun) ,另一种转换方法	
	@staticmethod #装饰器
	def staticFun():
		print Milo.name  #静态方法不许要加self，加类名
		print "我是静态方法"
	# staticNewFun = staticmethod(staticFun) ,另一种方法

zou = Milo()
zou.fun1()
zou.classFun()
Milo.staticFun()
