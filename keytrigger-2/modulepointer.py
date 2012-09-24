## modulepointer
# 
from imports import *

aliases = {}

__moduleList__ = os.listdir("modules")
for module in __moduleList__:
	modulename = ''.join([i for i in module][:-3])
	try:
		moduleKey = "from " + modulename + " import *"
		if DEBUG:
			print moduleKey
		exec moduleKey
	except Exception, e:
		if DEBUG:
			print "Failed to load module:", module, modulename, ":"
			print e
		else:
			pass
if DEBUG:
	print "Modules loaded."
