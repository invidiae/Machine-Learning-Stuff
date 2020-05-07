import matplotlib.pyplot as plt
import numpy as np
import math
import time
# set x
x = np.linspace(1,100,100)


saved = {}

def fib(num):
	if num in saved:
		return saved[num]
	else:
		if num == 0:
			return 0
		elif num == 1:
			return 1
		result = (fib(num-1)+fib(num-2))
		saved[num] = result
		return result
fi = [fib(i) for i in x]

s = [i**2 for i in x]

# factorial
safed_fac = {}
def fac(num):
	if num in safed_fac:
		return safed_fac[num]
	else:
		if num == 0:
			return 1
		result =  num*fac(num-1)
		safed_fac[num] = result
		return result
fa = [fac(i) for i in x]

#eX
eX = [math.e**i for i in x]


#plotting
plt.plot(x,fi, label= "fibunacci")
#plt.plot(x,s, label="square")
#plt.plot(x,fa, label = "factorial")
#plt.plot(x,eX, label = "e^x")
plt.legend(loc="best")
plt.show()






counter = 0

def move(f,t):
	print(f"Bewege von {f} nach {t}")
def hanoi(n, f, t, h):
	global counter
	if n == 0:
		pass
	else:
		hanoi(n-1,f,h,t)
		move(f,t)
		counter +=1
		print(counter)
		hanoi(n-1,h,t,f)





"""
def fib(num):
	if num == 0:
		return 0
	elif num == 1:
		return 1
	return(fib(num-1)+fib(num-2))

"""

