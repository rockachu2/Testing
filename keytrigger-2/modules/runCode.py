

## basic python interpreter module.
aliases.update({":", runCode})

def runCode(code):
	try:
		exec code
	except Exception, e:
		print e
