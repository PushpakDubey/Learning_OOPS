# WAP to select prime numbers in python

class SelectPrimeNumbers:

    def __init__(self):
        self.prime_numbers = []

    def select_prime_numbers(self, start, end):

        # Sieve of Eratosthenes
        # sieve = [True] * (end+1) # create a boolean list "sieve" of length "end+1" and set all values to True
        # for i in range(2, int(end ** 0.5) + 1): # iterate through the list from 2 to the square root of "end"
        #     if sieve[i]: # if the value at index "i" is True
        #         for j in range(i * i, end+1, i): # iterate through the list from "i*i" to "end+1" with a step of "i"
        #             sieve[j] = False # set all multiples of "i" to False
        # self.prime_numbers = [i for i in range(2, end+1) if sieve[i]] # create a list of prime numbers from 2 to "end+1" where the value at index "i" is True

        for i in range(start, end+1):
            if i > 1:
                for j in range(2, int(i ** 0.5) + 1):
                    if i % j == 0:
                        break
                    else:
                        self.prime_numbers.append(i)


numbers = SelectPrimeNumbers()
numbers.select_prime_numbers(1, 100)
print(numbers.prime_numbers)
