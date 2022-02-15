def add(a,b):
    return a+b

def fact(n):
	"""Computes the factorial of a natural number.
	
	Pre: -
	Post: Returns the factorial of 'n'.
	Throws: ValueError if n < 0
	"""
	total = 1
	for x in range(1,n+1):
		total=total*x
	return total



def roots(a, b, c):
	"""Computes the roots of the ax^2 + bx + x = 0 polynomial.
	
	Pre: -
	Post: Returns a tuple with zero, one or two elements corresponding
		to the roots of the ax^2 + bx + c polynomial.
	"""
	delta = b*b - 4*a*c
	print(delta)
	if delta > 0:
		root1 = (-b + delta)/(2*a)
		root2 = (-b - delta)/(2*a)
		return [root1,root2]
	elif delta == 0:
		root = -b/(2*a)
		return root
	elif delta < 0:
		return "Racine non réelle"

def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	pass

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, -3, 2))
	print(integrate('x ** 2 - 1', -1, 1))
