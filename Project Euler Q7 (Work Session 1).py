#10001th prime, problem 7 Project Euler
#Bill Zheng
#May 4, 2020


"""
Progress Work Session 1:
In this piece of code, I tried to create a isprime function and a nthprime function. I have been successful in terms of analyzing the specific roles of each function. 
However, I think there are still difficulties in terms of putting both of the functions together. One of the biggest errors are that sometimes an odd square would 
result in a return of True. I will try to add print statements to check where it goes wrong. The next step would be to integrate both of the functions together.
"""

from math import *


#The isprime function will test whether the number is prime or not. The next step is to create a list of prime numbers.
def isprime(n):
	for i in range(2, int(sqrt(n))+1):
		#only to square root is necessary
		if n % i == 0:
			print("False")
			return False
		else:
			print("True")
			return True


"""
Code in progress (counting all primes)
def primecounter(n):
	#find out what is the nth prime number
	nthprime = 1
	i = 3
	if isprime(i) == True:
		nthprime += 1
		i += 2
	elif isprime(i) == False:
		nthprime = nthprime
		i += 2
	if n == nthprime:
		print(i)
		return i
"""

if __name__ == "__main__":
	isprime(17312947)
	#Test Cases
