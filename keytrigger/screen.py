
def initDisplay():
	return changeableDisplay()



class changeableDisplay(object):
	def __init__(self):
		init()
		self.screen = pygame.display.set_mode((400,20))
		self.font = pygame.font.SysFont("Lucida Console", 12)
		self.messageText = ""

	def getUntilEnter(self, show=True):
		self.input = ""
		continuing = True
		while continuing:
			## add blinking cursor?
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_BACKSPACE:
						self.input = ''.join([i for i in self.input][:-1]) ## holy crap I need to fix this later #FIXME
					elif event.key == pygame.K_RETURN:
						continuing = False
					else:
						self.input += event.unicode
			if show:
				self.messageText = self.input
			else:
				self.messageText = "*" * len(self.input)
			self.draw(events=False) ## doesn't poll events
		return self.input

	def message(self, messageText):
		self.messageText = messageText ## conflict with function name *facepalm*
		self.draw()
		print "Drawn:", messageText


	def wait(self, endTime):
		self.update()
		now = 0
		while now < endTime: ## goddamn module names...
			now += 10
			time.sleep(0.01)
			self.update()

	def waitForKey():
		while True:
			pygame.display.update()
			if [event for event in pygame.event.get() if event.type == pygame.KEYDOWN] != []:
				return
			## FIX LATER uglyness



	def draw(self, events=True):
		self.screen.fill((0,0,0))
		self.screen.blit(self.font.render(self.messageText, 4, (255,255,255)),(0,0)) ## white
		if events:
			self.update()
		else:
			pygame.display.update()

	def update(self):
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					print "Uhm, dont know what to do here"
					#self.deInit()

	def deInit(self):
		pygame.quit()