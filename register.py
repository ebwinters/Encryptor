#!/user/bin/env python3
from encryptor import *
from peewee import *
from termcolor import colored, cprint
from collections import OrderedDict
import sys
import os
import getpass

db = SqliteDatabase('users.db')
is_signed_in = False
class User(Model):
	username = CharField(unique=True, primary_key=True, max_length=30)
	password = CharField(max_length=30, null=False)
	class Meta:
		database = db

def initialize():
	"""Create the database and table"""
	db.connect()
	db.create_tables([User], safe=True)

def menu_loop():
	"""Show the menu"""
	choice = None

	while choice != 'q':
		print("Press 'q' to quit")
		for key, value in menu.items():
			print('{}) {}'.format(key, value.__doc__))
		choice = input("Choice: ").lower().strip()

		if choice in menu:
			menu[choice]()

def create_user():
	"""Create an account"""
	user = input("Username: ")

	pprompt = lambda: (getpass.getpass(), getpass.getpass('Retype password: '))

	p1, p2 = pprompt()
	while p1 != p2:
	    print('Passwords do not match. Try again')
	    p1, p2 = pprompt()

	User.create(username=user, password=p1)
	print('user created')
	sign_in()

def sign_in():
	"""Sign in"""
	clear()
	print("This is the sign in screen")
	u = input("Username: ")
	p = input("Username: ")
	#query
	realp = (User.get(User.username==u).password)
	if p == realp:
		print("user is real")
		is_signed_in = True
	else:
		print("fuck you")


def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

menu = OrderedDict([
	("c", create_user),
	("s", sign_in),
	])

if __name__ == '__main__':
	initialize()
	menu_loop()

#Now that encryptor is imported, call menu loop and see if it works...
