import sys
import os
import datetime
import random
from collections import OrderedDict


def door_0(num):
	return num-2

def door_1(num):
	return num+3

def door_2(num):
	return num%10

def door_3(num):
	return num*6

def door_4(num):
	return num+9

def door_5(num):
	return num-5

def door_6(num):
	return num*3

def door_7(num):
	return num+8

def door_8(num):
	return num+0

def door_9(num):
	return num-10


door_select = {
	'zero': door_0,
	'one': door_1,
	'two': door_2,
	'three': door_3,
	'four': door_4,
	'five': door_5,
	'six': door_6,
	'seven': door_7,
	'eight': door_8,
	'nine': door_9,
	}





def hash(letter):
	list_index = None
	string_random = ''
	print ('\n')
	temp = ord(letter)
	print (temp)
	random_number = random.randrange(0, 10, 1)
	print(random_number)

	#stupid if statements since I clearly am incapable of working with ints in a tuple
	if random_number == 0:
		string_random = 'zero'
		list_index = 0
	if random_number == 1:
		string_random = 'one'
		list_index = 1
	if random_number == 2:
		string_random = 'two'
		list_index = 2
	if random_number == 3:
		string_random = 'three'
		list_index = 3
	if random_number == 4:
		string_random = 'four'
		list_index = 4
	if random_number == 5:
		string_random = 'five'
		list_index = 5
	if random_number == 6:
		string_random = 'six'
		list_index = 6
	if random_number == 7:
		string_random = 'seven'
		list_index = 7
	if random_number == 8:
		string_random = 'eight'
		list_index = 8
	if random_number == 9:
		string_random = 'nine'
		list_index = 9
	print(string_random)

	switched_int = door_select[string_random](temp)
	print(switched_int)





final_hash = ''
word = input("Input a word: ")
letter_list = list(word)
print(letter_list)
for char in letter_list:
	hash(char)





# letter = input("Enter a letter: ")
# print(ord(letter))

# number = int(input("Enter a number: "))
# print(door_1(number))

