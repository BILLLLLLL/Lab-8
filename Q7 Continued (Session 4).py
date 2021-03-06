#Bill Zheng
#May 12, 2020

"""
This is an attempt to integrate the isprime function with the prime counter function. The explanations are below on how this function will work.
One of the biggest problems is that the code is buggy. I have ran the code through python tutor, and I am thinking to make any changes.
However, I do hope that the structure of the code stays the same as my research have suggested that this is the most efficient way of doing it.
"""

def primecounter(k):
  #this function is set to find out what is the kth prime
	primelist = [2, 3, 5, 7, 11, 13]
  #this is the original 6 primes that will become the basis of the list
	nthprime = 5
  #this is the index of the list, which is one less than the actual kth prime
	n = 15
  #this is a good start with a number 2 bigger than 13
	for i in primelist and i <= int(sqrt(n)+1):
    #this incorporates the principles of only needing to test it to the square root
		if n % i == 0:
			n += 2
    #prime testing method. If it's composite, move on and add 2 to n
		else:
			n += 2
			nthprime += 1
			primelist.append(n)
      #if it is prime, then we add on to n
	if nthprime + 1 == k:
		print(primelist[nthprime])
		return primelist[nthprime]
    #this is for printing the kth prime
