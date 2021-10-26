def sum_of_digit():
    n = input("Введите трехзначное число: ")
    n = int(n)

    a = n % 10
    b = n % 100 // 10
    c = n // 100
    return a + b + c
print(sum_of_digit())