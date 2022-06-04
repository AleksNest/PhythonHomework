# print ('Задача 1. Ввычислить число пи, (использовать Ряд Нилаканта c заданной точностью.')

# d = int (input ('введите точность расчета ПИ - кол знаков дробной части: '))     # точность вычисления числа ПИ
# n = 1 / (10**(d+1)) 
# sgn = 1
# s = 3
# pi = 3.141592653589793238462643
# i = 2
# while (abs (pi - s) >= n):
#     s += ((sgn*4)/(i*(i+1)*(i+2)))
#     sgn = -sgn
#     i += 2

# print (f'расчетное число ПИ = {round(s,d)}')
# print (f'точность = {d} цифр после запятой')
# print ('кол итерраций = ', i/2)

# input()

# print ('Задача 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N..')

# N = int (input ('введите натуральное число: '))
# list_num = []
# i = 2
# while N !=1:
#     if (N % i == 0):
#         list_num.append(i)
#         N = N / i
#     else: 
#         i += 1
# print (list_num)

# while i <= N:
#     if (i % i == 0 ):
#         print (i)
#         i += 1

# input()

# print ('Задача 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности..')

# from random import randint
# L = []
# L_new = []
# for i in range (20):                                
#     L.append(randint(0,20))                     
   
# print ('исходная последовательность:')
# print (L)
# L.sort()
# for i in range(len(L)-1):
#     if (L[i] != L[i+1]):
#         L_new.append(L[i])
# print (L_new)

# input()


print ('Задача 4. Задана натуральная степень n. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени пример записи в файл ')
print ('при n=3 ==> 33x^3 + 8x^2 + 64x + 85 = 0 при n=2 ==> 27x^2 + 95x + 79 = 0.')

from random import randint as rnd

n = int (input ('введите степень: '))
def polynomial (n):
    equation = ''
    for i in range(n, 1, -1):
        k = rnd(0,100)
        if k != 0:
            equation += str(k) + 'x^' + str(i) + ' + '
        else:
            equation += ''
    equation += str(rnd(0,100)) + 'x' + ' + ' + str(rnd(0,100)) + ' = ' + '0'
    return equation
print (polynomial (n))

with open ('file1.txt', 'w') as data:
    data.write( polynomial (n))

print ('Задача 5. Даны два файла, в каждом из которых находится запись многочлена.') 
print ('Задача - сформировать файл, содержащий сумму многочленов. (нужно два полинома сложить. Файлы взять благодаря предыдущему заданию')

from functools import reduce

with open ('file2.txt', 'w') as data:
    data.write( polynomial (n))

import re
with open('file1.txt', 'r') as F1:          
    L1 = F1.read()
L1_new = []
L1_new = list(map(int,(re.findall('\d+', L1))))

with open('file2.txt', 'r') as F2:          
    L2 = F2.read()
L2_new = []
L2_new = list(map(int,(re.findall('\d+', L2))))

i = 0
s = ''
k = 0
equation = ''
for i in range(0, 2*n-2, 2):
    equation += str(L1_new[i]+L2_new[i]) + 'x^' + str(n-k) + ' + '
    k += 1
equation += str(L1_new[-3]+L2_new[-3] ) + 'x' + ' + ' + str (L1_new[-2]+L2_new[-2])+ ' = ' + '0'

with open ('file_rezult.txt', 'w') as data:
    data.write( equation)

print('В файле сумма многочленов: file_rezult.txt = file1.txt + file2.txt')    
