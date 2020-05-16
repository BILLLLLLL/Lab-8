#10001th prime, problem 7 Project Euler
#Bill Zheng
#May 15, 2020

"""
For my final code, I did a major overhaul of my original code as I believed that the original code cannot work due to errors in the for loop
of the application of the prime list. Because of that, I reverted back to my original design as I think an efficiency of O(n^3/2) is
acceptable for the program considering 10000 is not as big as it was thought. My final answer was proven correct, which return a value
of 104731, which is what others have got in their answers. Even though in the long run, my code is not maximized in terms of efficiency,
I think it works best because it takes less lines to run and it has a negligible running time in this scale. 

My final code consists of 2 functions, a function that tests whether a number is prime, and a function that indexes all prime numbers.
I chose to put both of them separately, and they ran efficiently.
"""

from math import *


#The isprime function will test whether the number is prime or not. The next step is to create a list of prime numbers.
def isPrime(n):
	for i in range(2, int(sqrt(n)) + 1):
    	#only a test to square root is necessary due to identities discussed in research
		if n % i == 0:
			return False
	return True
  	#I removed the else statement because if the prime test does not give a result then the number is automatically prime. Other tests are not necessary because 
  	#I set the original number to be 3, which is bigger than 1 or other messy numbers smaller than 0.

def primecounter(k):
	nthprime = 1
  	#this is the number of primes there
	primesuspect = 3
  	#The assumed prime, 3 is the starting prime
	while nthprime < (k - 1):
    	#k-1 is used to prevent overcounting
		if isPrime(primesuspect) == True:
			primesuspect += 2
			nthprime += 1
      	#if it is a prime, then we add 1 to the counter, and we add 2 (all even numbers are composite except 2)
		else:
			primesuspect += 2
      	#if not prime, add 2 and move on.
	return primesuspect

print(primecounter(10001))
