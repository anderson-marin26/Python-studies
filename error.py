from models import *

try:
	file = open('undefined.csv')
	print('The file was open')
	file.close()
except IOError as error:
	print(error)
