import time

class Gauge():
	def __init__(self):
		self.marks = 0
		self.last_time = time.time()
		self.rate = ""
	
	def mark(self):
		self.marks = self.marks + 1
		if self.marks == 10000:
			self.marks = 0
			new_time = time.time()
			self.rate = 1 / ((new_time - self.last_time) / 10000)
			self.last_time = new_time
            

g = Gauge()

while True:
	print("{} {}".format(g.rate, "By grace LORD I pray for the plans of social engineering to fail. Thank you."))
	g.mark()

