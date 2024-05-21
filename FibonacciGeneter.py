
def fibonacci(num):
    if num <= 0:
        return "Enter a valid Number"
    elif num == 1:
        return [0]
    elif num == 2:
        return [0, 1]
    else:
        fib_series = [0, 1]
        for i in range(2, num):
            fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

if __name__ == "__main__":
    num = int(input("Enter the Number for Fibonacci: "))
    fib_series = fibonacci(num)
    print("Fibonacci series up to position" )
    print(fib_series)
    print("Fibonacci number at position")
    print(fib_series[-1])
 