from imports import *

if DEBUG:
	from debugtools import *


def startTerm():
	child = subprocess.Popen([sys.executable, "term.py"])
	if DEBUG:
		subprocessPrint(child) ## debugtools reference