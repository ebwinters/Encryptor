#!/user/bin/env python3
#imports
from peewee import *
from termcolor import colored, cprint
from collections import OrderedDict
import sys
import os
import datetime



db = SqliteDatabase('encryptor.db')

class Message(Model):
	content = TextField()
	code = CharField()
	timestamp = DateTimeField(default=datetime.datetime.now)
	class Meta:
		database = db

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

def read_message():
	"""Read an encrypted message to the database"""

def search_for_code():
	"""Search the database for a code to receive a message"""

menu = OrderedDict([
	("'send'", send_message),
	("'read'", read_message),
	])

if __name__ == '__main__':
	initialize()
	menu_loop()




