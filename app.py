# -*- coding: UTF-8 -*-

def search(names):
	print('Buscar:')
	name = input()

	if(name in names):
		position = names.index(name)

		print('Encontrado')
		print(names[position])
	else:
		print('Não foi encontrado')

def change(names):
	print('Qual nome deseja alterar')
	name = input()
	if(name in names):
		position = names.index(name)
		print('Alterar %s para?' % (names[position]))
		new_name = input()
		names[position] = new_name
	else:
		print('Nome não encontrado')

def remove(names):
	print('Qual nome deseja remover?')
	name = input()
	names.remove(name)

def list(names):
	print('Listando nomes: ')
	for name in names:
		print(name)

def register(names):
	print('Digite o nome: ')
	name = input()
	names.append(name)
	return names

def menu():
	names = []
	action = ''
	while(action != '0'):
		print('Digite 1 para cadastrar, 2 para listar, 3 para remover, 4 para alterar, 5 para buscar, 0 para terminar')
		action = input()

		if(action == '1'):
			register(names)

		if(action == '2'):
			list(names)

		if(action == '3'):
			remove(names)

		if(action == '4'):
			change(names)

		if(action == '5'):
			search(names)

menu()
