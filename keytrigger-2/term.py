## term.py


# ought to load command tools and have an option to run actual python code as the file.

from imports import *

from modulepointer import *

## mainloop

__exiting__ = False

while not __exiting__:
	__command__ = raw_input(interpreter.symbol)

	__command__ = __command__.split() ## splits at whitespace

	try:
		__running__ = aliases[__command__]