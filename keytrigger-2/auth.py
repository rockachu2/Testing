from imports import *

import hashlib
import getpass
if DEBUG:
	print "Importing successful"

try:
	passwordInput = getpass(passwordPrompt)
except Exception, e:
	if DEBUG: print e
	else:
		sys.exit()

if DEBUG: print "Grabbed Password"