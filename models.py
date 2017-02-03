# -*- coding: UTF-8 -*-

class Profile(object):
	def __init__(self, name, phone, company):
		self.name = name
		self.phone = phone
		self.company = company

	def print(self):
		print('Nome: %s, Telefone: %s, Empresa: %s' % (self.name, self.phone, self.company))
