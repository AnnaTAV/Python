# 3 Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
# Рост матерей 178, 165, 165, 173, 168, 155, 160, 164, 178, 175
# Используя эти данные построить 95% доверительный интервал для разности среднего 
# роста родителей и детей.


import numpy as np
import scipy.stat as stats
arrDaughter=np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
arrMother=np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
len(arrDaughter)
len(arrMother)


arrDaughter=np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
x_Daughter=np.mean(arrDaughter)
D_Daughter=np.var(arrDaughter, ddof=1)
print(f'Среднее выборочное 1: {x_Daughter},\n'
      f'Размер выборки n1={len(arrDaughter)},\n'
      f'Несмещенная дисперсия для выборки 1: {D_Daughter}.')


arrMother=np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
x_Mother=np.mean(arrMother)
D_Mother=np.var(arrMother, ddof=1)
print(f'Среднее выборочное 1: {x_Mother},\n'
      f'Размер выборки n2={len(arrMother)},\n'
      f'Несмещенная дисперсия для выборки 2: {D_Mother}.')

delta = x_Daughter - x_Mother
print(f'Дельта: {delta},\n')
D = (D_Daughter+D_Mother)/2
print(f'Объединенная оценка дисперсии: {D},\n')
SE = np.sqrt(D/10+D/10)
print(f'Стандартная ошибка разности средних: {SE},\n')

# Для вычисления t-критерия воспользуемся библиотекой scipy

import scipy.stats as stats
t = stats.t.ppf(0.975, 18) 
# степени свободы 2*(n-1)=2*(10-1) = 18
print(f'Табличное значение t-критерия для 95%-го доверительного интервала данной выборки: {t},\n')

L = delta - t * SE
print(f'нижняя граница интервала: {L},\n')
U = delta + t * SE
print(f'верхняя граница интервала: {U},\n')