# WAP to select even numbers in python
class SelectEvenNumbers:

    def __init__(self):
        self.even_numbers = []

    def select_even_numbers(self, start, end):
        for i in range(start, end+1):
            if i%2 == 0:
                self.even_numbers.append(i)

numbers = SelectEvenNumbers()
numbers.select_even_numbers(20, 10000001)
print(numbers.even_numbers)