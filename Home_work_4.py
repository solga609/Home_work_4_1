# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001

# out
# 8.988

num = float(input("Enter a real number: "))
accu = input("enter the required accurancy '0.0001' : ").split(".")
print(f"{num:.{len(accu)}f}")

# 2.Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

def Factor(n):
    Num = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Num.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Num.append(n)
    return Num
print(Factor(int(input())))


# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

numbers = [1, 2, 5, 4, 6, 5, 4, 2, 9]

def get_unique_numbers(numbers):
    list_of_unique_numbers = []
    unique_numbers = set(numbers)

    for number in unique_numbers:
        list_of_unique_numbers.append(number)

    return list_of_unique_numbers


print(get_unique_numbers(numbers))




