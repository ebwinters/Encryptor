#!/user/bin/env python3
#imports
from peewee import *
from termcolor import colored, cprint
from collections import OrderedDict
import sys
import os
import datetime
import random



db = SqliteDatabase('encryptor.db')

class Message(Model):
	content = TextField()
	code = CharField()
	timestamp = DateTimeField(default=datetime.datetime.now)
	class Meta:
		database = db
#necessary stuff
def door_0(num):
	return num-2

def door_1(num):
	return num+3

def door_2(num):
	return num*10

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

random_number_list = []
switched_int_list = []

def initialize():
	"""Create the database and table"""
	db.connect()
	db.create_tables([Message], safe=True)

def menu_loop():
	"""Show the menu"""
	clear()
	choice = None

	while choice != 'q':
		print("Press 'q' to quit")
		for key, value in menu.items():
			print('{}) {}'.format(key, value.__doc__))
		choice = input("Choice: ").lower().strip()

		if choice in menu:
			menu[choice]()

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

def send_message():
	"""Send an encrypted message"""
	clear()
	# def door_0(num):
	# 	return num-2

	# def door_1(num):
	# 	return num+3

	# def door_2(num):
	# 	return num%10

	# def door_3(num):
	# 	return num*6

	# def door_4(num):
	# 	return num+9

	# def door_5(num):
	# 	return num-5

	# def door_6(num):
	# 	return num*3

	# def door_7(num):
	# 	return num+8

	# def door_8(num):
	# 	return num+0

	# def door_9(num):
	# 	return num-10


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



	#hash() vars
	
	def hash(letter):
		list_index = None
		string_random = ''
		print ('\n')
		temp = ord(letter)
		# print (temp)
		random_number = random.randrange(0, 10, 1)
		# print(random_number)

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
		# print(string_random)

		switched_int = door_select[string_random](temp)
		# print(switched_int)

		random_number_list.append(random_number)
		# print(random_number_list)

		switched_int_list.append(switched_int)
		# print(switched_int_list)

	def key():
		return random_number_list

	def value():
		return switched_int_list





	final_hash = ''
	word = input("Input a message: ")
	letter_list = list(word)
	# print(letter_list)
	for char in letter_list:
		hash(char)
	list1 = key()
	list2 = value()
	# print(list1)
	# print(list2)
	stringlist_key = ''.join(str(n) for n in list1)
	stringlist_value = ''.join(str(n) for n in list2)
	# print(stringlist_key)
	# print(stringlist_value)

	data = stringlist_value
	code = stringlist_key
	if data:
		if input("Send message? [y/n] ").lower() == 'y':
			Message.create(content=data, code=code)
			print('Message sent')
			print('Copy this key, you will need it to receive a message code: ')
			cprint(code, 'green')


def read_message(search_query=None):
	"""Read an encrypted message to the database"""
	clear()
	messages = Message.select()

	if search_query:
		messages = messages.where(Message.code.contains(search_query))

	for msg in messages:
		print('='*60)
		print(msg.content)
		decrypt_choice = input('Would you like to decrypt this message? [y/n] ').lower()
		if decrypt_choice != 'n':
			decrypt_message(msg)


def search_messages():
	"""Search entries for a string"""
	read_message(input("Message code: "))

def decrypt_message(message):
	"""Decrypt a message"""
	final_string = ''
	tracker = 0
	# messages = Message.select()
	# instance = messages.where(Message.content.contains(message))
	while tracker < len(switched_int_list):
		temp_rand = random_number_list[tracker]
		temp_switched = switched_int_list[tracker]
		real_value = None

		if temp_rand == 0:
			temp_switched = int(temp_switched + 2)
		if temp_rand == 1:
			temp_switched = int(temp_switched - 3)
		if temp_rand == 2:
			temp_switched = int(temp_switched / 10)
		if temp_rand == 3:
			temp_switched = int(temp_switched / 6)
		if temp_rand == 4:
			temp_switched = int(temp_switched - 9)
		if temp_rand == 5:
			temp_switched = int(temp_switched + 5)
		if temp_rand == 6:
			temp_switched = int(temp_switched / 3)
		if temp_rand == 7:
			temp_switched = int(temp_switched - 8)
		if temp_rand == 8:
			temp_switched = int(temp_switched + 0)
		if temp_rand == 9:
			temp_switched = int(temp_switched + 10)
		final_string = final_string + chr(temp_switched)

		tracker = tracker + 1

	print("The message reads as follows: ")
	cprint(final_string, 'green')
	delete_choice = input("Do you want this message to automatically delete? [y/n]: ").lower()

	if delete_choice != 'n':
		delete_message(message)
	if delete_choice == 'n':
		menu_loop




def delete_message(message):
	message.delete_instance()
	print('Message is erased now')

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')
# def search_for_code():
# 	"""Search the database for a code to receive a message"""

menu = OrderedDict([
	("send", send_message),
	("read", search_messages),
	])



if __name__ == '__main__':
	initialize()
	menu_loop()




