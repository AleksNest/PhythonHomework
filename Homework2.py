print ('Задача 1. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N ')

from math import factorial
n = int(input ('введите N: '))
List = []
j= 1
for i in range(n):
    List.append(factorial(j))
    j += 1
print (List)

input()

print ('Задача 3. Алгоритм перемешивания списка ')
import random
import time
print ('исходный список:', end = '     ')
list = [1, 'world', -100, 2.5, 'привет']
print (list)
while True:
    random.shuffle(list)
    print ('перемешанный список:', list)
    time.sleep(1)
input()




print ('Задача 2. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму. Нахождение экспоненты')
n = int(input ('введите N: '))
Dict = {}
rezult = 0
for i in range(1, n+1):
    Dict[i] = round ((1+1/(i))**i, 4)
    rezult += Dict[i]
print (Dict)
print (f'сумма значений =  {rezult}; Dict[{n}] = {Dict[n]}')
