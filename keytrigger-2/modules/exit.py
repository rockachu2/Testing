
aliases.update({"exit":__exit__cause_exit()})
aliases.update({"quit":__exit__cause_exit()})

def __exit__cause_exit(args):
	if args:
		print "No args supported" ## FIXME
	global __exiting__
	__exiting__ = True
