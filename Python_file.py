def fibonacci(num):
    n1 = 0
    n2 = 1
    series = 0
    for i in range(num):
        print(series, end=' ');
        n1 = n2;
        n2 = series;
        series = n1 + n2;
 
num = int(input('Number Fibonacci serie: '))
fibonacci(num)
