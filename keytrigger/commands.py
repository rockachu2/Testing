import pyHook
import pyHook
import pythoncom
import ctypes
import subprocess
import sys


def onKeyboardEvent(event):
	## test
	#print event.KeyID ## debug
	if event.KeyID == 19:## pausebreak key
		child = subprocess.Popen([sys.executable, "commander.py"])## DEBUG
	return True

if __name__ == "__main__":
	hookManager = pyHook.HookManager() 
	hookManager.KeyDown = onKeyboardEvent
	hookManager.HookKeyboard()
	print "Initialization successful"
	pythoncom.PumpMessages()