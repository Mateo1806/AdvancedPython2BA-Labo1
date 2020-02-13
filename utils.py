# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018
from math import sqrt

def fact(n):
	x = 1
	for i in range (0,n):
		x = x*(i+1)
	return x

def roots(a, b, c):
	d = b**2 - 4*a*c
	if d < 0 :
		return ()
	if d == 0:
		return ((-b )/(2*a),) #virgule après la parenthèse sinon il considère comme un nombre et pas comme un tuple
	if d > 0 :
		return ((-b + sqrt(d))/(2*a), (-b - sqrt(d))/(2*a))

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
	x = 1
	try:
		_ = eval (function) #_ c'est une variable qui n'est pas utilisée
	except:
		"error in fuction"
	if upper < lower:
		return "upper is smaller than lower bound"
	from scipy import integrate
	fct = lambda x: eval(function)
	result = integrate.quad(fct, lower, upper)
	return result[0]
	

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
