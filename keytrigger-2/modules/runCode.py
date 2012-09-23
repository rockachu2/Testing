

## basic python interpreter module.
aliases.update({":", __runCode__runCode})

def __runCode__runCode(code):
	try:
		exec code
	except Exception, e:
		print e
