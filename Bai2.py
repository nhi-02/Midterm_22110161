def factorial(n):
    if n < 0:
        print('nhap so nguyen khong am')
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        factor = 1
        for i in range(2, n + 1):
            factor *= i
        return factor


n = int(input('Nhap mot so nguyen khong am: '))

if n >= 0:
    print(f'Giai thua cua {n} la: {factorial(n)}')
else:
    print('nhap mot so nguyen khong am')