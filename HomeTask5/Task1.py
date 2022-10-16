# 1.	Напишите программу, удаляющую из текста все слова, содержащие "абв".


n = 'Решение задачи №1 5-го домашнего задания'.split()
print (n)
result = filter(lambda x: 'а' not in x and 'б' not in x and 'в' not in x, n)
print (*result)
