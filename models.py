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

class ProfileVip(Profile):
	def __init__(self, name, phone, company, nick):
		super(ProfileVip, self).__init__(name, phone, company)
		self.nick = nick

	def get_credits(self):
		return super(ProfileVip, self).get_likes() * 10.0