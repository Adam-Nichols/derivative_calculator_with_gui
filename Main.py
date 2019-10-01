import sympy

function = input("Please enter the fucntion you would like to differentiate: ")
derivative_variable = sympy.Symbol(input("Which function would you like to differentiate with respect to? "))

first_derivative = sympy.diff(function, derivative_variable)
first_derivative.doit()

print(first_derivative)

