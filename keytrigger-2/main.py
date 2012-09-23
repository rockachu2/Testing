from imports import *


import pyHook as pyhook
import pythoncom
import subprocess
import sys


def startTerm():
	child = subprocess.Popen([sys.executable, "auth.py"])
	if DEBUG:
		subprocessPrint(child) ## debugtools reference


def handleKeypress(event):
	if DEBUG: 
		print event.Ascii,
		print chr(event.Ascii)
	if event.Ascii == 96:
		startTerm()
		return False

	return True


def initHooks():
	hookManager = pyhook.HookManager()
	hookManager.KeyDown = handleKeypress
	hookManager.HookKeyboard()

def hookStart():
	pythoncom.PumpMessages()


initHooks()
hookStart()