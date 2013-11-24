#coding:utf8

class Milo():
	var1 = "类属性，公有属性var1"
	__var2 = "类的私有属性 __var2"

	def fun(self):
		self.var2 = "对象的公有属性var2"
		self.__var3 = "对象的私有属性 __var3"
		var4 = "函数 fun的 局部变量 var4"

zou = Milo()
zou.fun()
print zou.var1
print zou.var2
