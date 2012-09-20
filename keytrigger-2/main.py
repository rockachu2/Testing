from imports import *
from hooking import *

if DEBUG:
	from debugtools import *


def startTerm():
	child = subprocess.Popen([sys.executable, "auth.py"])
	if DEBUG:
		subprocessPrint(child) ## debugtools reference


hookStart()