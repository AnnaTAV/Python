# На сколько сигм (средних квадратичных отклонений) отклоняется рост человека, равный 190 см, от
# математического ожидания роста в популяции, в которой M(X) = 178 см и D(X) = 25 кв.см?

# Рассчитаем Z

Z=(190-178)/25**(1/2)
# Z = 2,4
print(f'Рост человека, равный 190 см, отклоняется от математического ожидания роста в популяции, \n'
      f'в которой M(X) = 178 см и D(X) = 25 кв.см на Z = {Z} сигм.')