import sys

import parse as p
import compute as c

def main():
	args = sys.argv[1:]
	if not args:
		get_input = input("Enter a polynomial equation: ")
		args = [get_input]
	if len(args) > 1:
		equation = p.concatenate(args)
	else:
		equation = args[0]

	equation = p.reduce(equation)
	p.parse(equation)
	c.compute(equation)

if __name__ == "__main__":
	main()