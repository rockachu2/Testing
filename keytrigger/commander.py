## commander custom build

## hook to the key pause/break, then pop opne a GUI so as to run custom command. 
## soon to support modules.]
import pygame
from pygame import *

import sys
import os
import time
import hashlib ## for passwords

def init():	## needs to be called many times
	pygame.init()
	pygame.font.init()

def exit():
	pygame.quit()
	sys.exit()

init()

from screen import *

def initTerm():
	startTerm(getPass())



def getPass():
	display = initDisplay()
	print "b"
	display.message("Password:") ## FIXME
	print "c"
	password = display.getUntilEnter(show=False)
	hash = hashlib.sha512(password).hexdigest()
	del password
	try:
		passFile = open("password", 'r')
		baseHash = passFile.readline()
		passFile.close()
	except:
		display.message("Error reading from password file.")
		return False
	print "d"
	if hash == baseHash:
		display.deInit()
		return True
	else:
		display.message("Wrong Password")
		display.wait(1000)
		display.deInit()
		return False
	

def loadCommands():
	files = os.listdir("commands")
	knownCommands = {}
	
	## HERE COMES THE NIGHTMARE
	from commands import lockScreen
	from commands import python as pythonesque
	knownCommands["lock"] = lockScreen.start
	knownCommands[":python"] = pythonesque.start

	return knownCommands


def startTerm(identification):
	print "e"
	if identification == False:
		return 0 ## end session
	else: 
		pass ## we are ok here
	display = initDisplay()
	display.message("Loading commands...")
	display.wait(1000)
	knownCommands = loadCommands() ## returns dictionary

	## mainloop
	while True:
		fullCommand = display.getUntilEnter(":")
		rootCommand = fullCommand.split(" ")
		print fullCommand
		print rootCommand ## DEBUG
		if rootCommand in knownCommands.keys():
			try:
				knownCommands[rootCommand](fullCommand)
			except Exception as e:
				display.message(e)
				display.waitForKey()
		else:
			display.message("Unknown Command:" + rootCommand)
			display.waitForKey()


	exit()



initTerm()