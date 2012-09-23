from imports import *

import hashlib
from getpass import getpass
if DEBUG:
	print "Importing successful"

try:
	passwordInput = getpass(passwordPrompt)
except Exception, e:
	if DEBUG: print e
	else:
		sys.exit()

if DEBUG: print "Grabbed Password"

try:
	saltFile = open(authDir + "salt", 'r')
	hashFile = open(authDir + "hash", 'r')
except Exception, e:
	if DEBUG: print e
	print "Unable to open password and salt files."
	sys.exit()

try:
	salt = saltFile.readline()
	hash = hashFile.readline()

	if DEBUG: print hash, salt, hashFile, saltFile



	hashObject = hashlib.sha512()
	hashObject.update(salt)
	hashObject.update(passwordInput)
	passwordHash = hashObject.hexdigest()

	if DEBUG: print passwordHash

	if passwordHash == hash:
		child = subprocess.Popen([sys.executable, "term.py"])
		if DEBUG: subprocessPrint(child) ## debugtools reference
except Exception, e:
	if DEBUG: print e
