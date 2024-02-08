# WAP to generate Fibonacci Series in python

class FibonacciSeries:

    def __init__(self):
        self.fibonacii_series = []

    def generate_fibonacii_series(self, series_limit):
        a, b = 0, 1
        for _ in range(series_limit):
            self.fibonacii_series.append(a)
            a, b = b, a + b

numbers = FibonacciSeries()
numbers.generate_fibonacii_series(100)
print(numbers.fibonacii_series)