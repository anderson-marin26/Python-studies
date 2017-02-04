# -*- coding: UTF-8 -*-

class Profile(object):
	def __init__(self, name, phone, company):
		self.name = name
		self.phone = phone
		self.company = company
		self.__likes = 0

	def print(self):
		print('Nome: %s, Telefone: %s, Empresa: %s' % (self.name, self.phone, self.company))

	def like(self):
		self.__likes+= 1

	def get_likes(self):
		return self.__likes

class Data(object):
   def __init__(self, day, month, year):
      self.day = day
      self.month = month
      self.year = year

   def imprime(self):
      print('%s/%s/%s' % (self.day, self.month, self.year))
