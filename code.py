#imports
from random import randint
import binascii
import math
def e(p, key):

	p_list = list(p)
	for char in p_list:
		ask = ord(char)
		right = ask*key
		intlist.append(right)
	stringlist_key = ''.join(str(n) for n in intlist)
	stringlist_key = stringlist_key + str(key)
	return stringlist_key
		






def d(c, key):
	for i in intlist:
		num = int(i/key)
		print(chr(num))


	




p = input("Input a string: ")
k = int(input("Input an int: "))
intlist = []
finalstr = ''
estring = e(p,k)
print(estring)
print(d(estring, k))



#encrypted code: 2312913483489631534596291963003513272949633630331529730396333306963453123153483







