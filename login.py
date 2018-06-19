import time
print("hello world")

def demo():
	return "ok!"
demo()

class Index(object):
	def __init__(self, name):
		self.name = name

	def demo_print(self):
		print(self.name)

tom = Index("xiaoming")
tom.demo_print()

time.sleep(1)
print("time")
