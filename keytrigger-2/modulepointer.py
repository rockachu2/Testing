## modulepointer
# 
from imports import *

aliases = {}

__moduleList__ = os.listdir("modules")
for module in __moduleList__:
	try:
		moduleKey = "from " + module + " import *"
		if DEBUG:
			print moduleKey
		exec moduleKey
	except Exception, e:
		if DEBUG:
			print "Failed to load module:", module, ":"
			print e
		else:
			pass
if DEBUG:
	print "Modules loaded."
