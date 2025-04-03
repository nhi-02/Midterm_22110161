def fibonacci_dp(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    fib = [0] * (n + 1)
    fib[0], fib[1] = 0, 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]  
    return fib[n]

num = int(input('Nhap so n: '))
print(fibonacci_dp(num))  
