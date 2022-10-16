# 3. Задайте список из n чисел последовательности (1 - 1 / n) ** n и выведите на экран их сумму.

# Пример:

# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037

N = int(input('Введите число N: '))
def progress(N):
    return[round((1 + 1 / a)**a, 2) for a in range (1, N + 1)]   
print(progress(N))
print(f'{N} -> {"%.3f" %(round(sum(progress(N))))}')

