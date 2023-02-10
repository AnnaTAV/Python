# На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень. 
# Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6. 
# Найти вероятность того, что выстрел произведен: a). первым спортсменом б). вторым спортсменом 
# в). третьим спортсменом.

# Рассмотрим следующие события:
# A  - в результате выстрела, цель поражена;
# B1 - выстрел произведен первым спортсменом;
# B2 - выстрел произведен вторым спортсменом;
# B3 - выстрел произведен третьим спортсменом.
# Вероятности того, что выстрел произведен определенным спортсменом равны, т.к. выстрел 1, 
# и произвести его могут только 3 этих спортсмена, т.е. события B1, B2, B3 составляют полную группу событий.
# => P(B1) = P(B2) = P(B3) = 1/3
# Вероятность того, что произошло событие A, при условии наступления события B
# PB1(A) = 0.9, PB2(A) = 0.8, PB3(A) = 0.6

import numpy as np
from math import factorial
PB=1/3
PA=PB*0.9+PB*0.8+PB*0.6
print(f'Полная вероятность наступления события А Р(А) = {PA: .4f}')

# Теперь, исходя из того, что событие A уже произошло, с помощью формулы Байеса оценим вероятность того, 
# что имело место одно из событий B

PAB1=PB*0.9/PA
PAB2=PB*0.8/PA
PAB3=PB*0.6/PA
print(f'Вероятность того, что выстрел произвёл первый спортсмен: {PAB1: .4f};\n'
      f'Вероятность того, что выстрел произвёл второй спортсмен: {PAB2: .4f};\n'
      f'Вероятность того, что выстрел произвёл третий спортсмен: {PAB3: .4f}.')