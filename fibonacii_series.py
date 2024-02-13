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

# But this is not the best way to generate fibonacii series, as it is not memory efficient
# So, we can use generator to generate fibonacii series
def generate_fibonacii_series_by_recursion(series_limit):
    if series_limit <= 1:
        return series_limit
    else:
        return generate_fibonacii_series_by_recursion(series_limit - 1) + generate_fibonacii_series_by_recursion(
            series_limit - 2)

print(generate_fibonacii_series_by_recursion(30))