from math import sqrt

def primecounter(k):
    primelist = [2, 3, 5, 7, 11, 13]
    #this is still in line with dividing only prime numbers to test whether a number is prime or not.
    nthprime = 5
    #13 is the 6th prime, therefore it gets a 5 as the index indicates, which is the reason why the value is 5
    n = 15
    #15 is the next odd number bigger than 13
    for i in primelist:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                n += 2
            #attempting to implement isprime(n) function here
            else:
            #if it is prime, then the prime counter adds one, n adds 2, appends the list, and resets the value of i
                n += 2
                nthprime += 1
                primelist.append(n)
            i = primelist[0]
                
    if nthprime + 1 == k:
        print(primelist[nthprime])
        return primelist[nthprime]
        
if __name__ == "__main__":
    primecounter(27)
