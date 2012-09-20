

def name():
	return ["lockScreen", "lock"]

def start():
	lockScreen()

import subprocess
def lockScreen():
	subprocess.call(["rundll32.exe", "user32.dll", "LockWorkStation"])