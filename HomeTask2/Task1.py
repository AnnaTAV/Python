# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Пример:

# 6782 -> 23
# 0,56 -> 11

N = input('Введите число N: ')
sum = 0
for i in str(N):
    if i != ".":
        sum += int(i)
print (f"{N} -> {sum}")