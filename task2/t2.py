# Задайте натуральное число N. Напишите программу, которая
# составит список простых множителей числа N.

num = int(input("Введите число: "))
n = 2
my_list = []
old = num
while n <= num:
    if num % n == 0:
        my_list.append(n)
        num //= n
        n = 2
    else:
        n += 1
print(f"Простые множители числа {old} -> {my_list}")