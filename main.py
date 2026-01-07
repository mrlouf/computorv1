import sys

from classes.computor import Computorv1

def main():
	c = Computorv1()

	args = sys.argv[1:]
	if not args:
		get_input = input("Enter a polynomial equation: ")
		args = [get_input]
	
	if len(args) > 1:
		c.equation = c.concatenate(args)
	else:
		c.equation = args[0]

	c.reduce()
	c.parse()
	c.compute()

if __name__ == "__main__":
	main()