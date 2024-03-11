def exponetialFunction(a,b,x):
    return a*b**x

def twoPointExponetial(x1,o1,x2,o2,nx):
    # a * b^x
    b = (o1/o2)**(1/(x1-x2))
    a = o2/(b**x2)
    print(a,'x',b,'^ x')
    print('The unknown output of',nx,'is',exponetialFunction(a,b,nx))

print("Your first 'x' value has to be \nsmaller than your second 'x' value \n")
x1 = float(input("Input your first x input: "))
o1 = float(input("Input your first y output: "))
x2 = float(input("Input your second x input: "))
o2 = float(input("Input your second y output: "))
nx = float(input("Input the 'x' value you want to solve for: "))

twoPointExponetial(x1,o1,x2,o2,nx)
