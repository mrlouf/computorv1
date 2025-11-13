import re

def parse(equation):
	pass

""" 
	This function parses the equation given and tries to reduce it to the canonical form
	of a second degree polynomial equation: ax^2 + bx + c = 0.
	If it cannot, it checks if the equation is of the first degree. If neither, then
	the equation is cubic or of a higher degree and therefore not supported.
"""
def reduce(equation):
	# Extract terms using regex
	terms = re.findall(r'([+-]?\s*\d*\.?\d*)\s*\*?\s*x\^2|([+-]?\s*\d*\.?\d*)\s*\*?\s*x|([+-]?\s*\d+)', equation)
	
	a, b, c = 0, 0, 0

	# DEBUG
	print(terms)

	for term in terms:
		if term[0]:  # x² term
			a += float(term[0].replace(' ', '') or '1')
		elif term[1]:  # x term
			b += float(term[1].replace(' ', '') or '1')
		elif term[2]:  # constant term
			c += float(term[2].replace(' ', ''))

	if a != 0:
		max_power = 2
	elif b != 0:
		max_power = 1
	else:
		max_power = 0

	if max_power > 2:
		raise ValueError("This program only handles first and second-degree equations.")
	elif max_power == 2:
		reduced = f"{a} * x^2 + {b} * x + {c} = 0"
	elif max_power == 1:
		reduced = f"{b} * x + {c} = 0"
	else:
		reduced = f"{c} = 0"

	print("Reduced form:", reduced)
	print("Polynomial degree:", max_power)
	return reduced

def concatenate(args):
	concatenated = string(''.join(args))
	return concatenated