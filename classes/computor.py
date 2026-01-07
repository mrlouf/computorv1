import parse as p
import compute as c

"""	Main class for the Computorv1 program."""
class Computorv1:
	def __init__(self):
		equation = ""
	def concatenate(self, args):
		return p.concatenate(args)
	def parse(self):
		p.parse(self.equation)
	def compute(self):
		c.compute(self.equation)
	def reduce(self):
		return p.reduce(self.equation)