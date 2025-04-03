def is_prime(n):
    if n <= 1:
        print(f'{n} khong phai so nguyen to')
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f'{n} khong phai so nguyen to')
            return False
    print(f'{n} la so nguyen to')
    return True

n = int(input('nhap so n: '))
is_prime(n)
