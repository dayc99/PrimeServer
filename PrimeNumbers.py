__author__ = 'joseph'

#Built in Python 3.4


class Prime_Number:
    """Class to find prime numbers"""

    def __init__(self):
        pass

    def sieve(self, number):
        """Return a list of the primes n and below."""

        #The first 3 numbers, 0,1,2 will ALWAYS correspond to false,false,and true
        #after that,we know that every multiple of 2 will ALWAYS be false so we do this
        #when we initialize the array to save time. Every odd number MAY be a prime
        #         0       1      2       3      4
        prime = [False, False, True] + [True, False] * (number // 2)

        #print out the prime array
        #print(prime)

        for number_in_array in range(3, int(number ** .5) + 1, 2):
            #print("Number at position p: %d" %p)
            if prime[number_in_array]:
                #make every number that is a multiple of that number false skipping even multiples
                for index in range(number_in_array * number_in_array, number + 1, 2 * number_in_array):
                    prime[index] = False
                    #print("Number we are changing to false: %d" %i)

        #return all numbers in array that are true to the inputted number
        return [p for p in range(2, number+1) if prime[p]]


    def primes(self, number):
        """Return a list of the primes n and below and if the inputted number was prime"""
        if isinstance(number, int):
            return self.sieve(self,number)
        else:
            return "Input is not an instance of integer"