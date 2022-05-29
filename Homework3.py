print ('Задача 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.')

my_list = [2, 3, 5, 9, 3, 10, 11]
def SumOfOddNumbers(List): 
    Summa = 0
    for i in range(len(List)): 
        if i % 2 != 0: 
            Summa = Summa + List[i] 
    return Summa
print ('исходный список: ',my_list)
print (f'сумма элементов на нечетных позициях: {SumOfOddNumbers(my_list)}')

input()

print ('Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.')
my_list = [2, 3, 4,  5, 6]
def MultiplicationNumbers(List): 
    list_multipl = []
    for i in range(int(len(List)/2)): 
        list_multipl.append(my_list[i]*my_list[len(List)-1-i])
    if (len(List)/2 % 2 != 0):
        list_multipl.append (my_list[(int(len(List)/2))]**2)
    return list_multipl
print ('исходный список',my_list)
print (f'произведение пар чисел: {MultiplicationNumbers(my_list)}')

input()

print ('Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным')
print (' и минимальным значением дробной части элементов.')
my_list = [1.1, 1.2, 3.1, 5, 10.01]
max = my_list[0] - int( my_list[0])
min = max
for item in my_list:
    fraction_part = item - int(item)
    if (fraction_part > max):
        max = fraction_part
    if (fraction_part < min and fraction_part !=0 ):
        min = fraction_part
print (f'дробной части элементов из списка {my_list} max - min: = {round((max-min),3)}')

input()

print ('Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.')
num = int(input('введите число: '))

def Dvcod (num):
    if (num < 0): num = -1*num
    while (num >= 1):
        DvFigura = str(num % 2)
        return  int(str (Dvcod (int (num / 2))) + DvFigura)
    else: return 0
        
if (num < 0 ): print (f' {num} = {-1*Dvcod (num)}')
else : print (f' {num} = {Dvcod (num)}')

input()

print ('Задача 5. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов..')
n = int(input('введите N  '))
def FibNega (n):
    if n ==-1:
        return 1
    if n == -2:
        return  -1
    else:
        return FibNega (n+2) - FibNega (n+1) 

def Fib (n):
    if n in [1, 2]:
        return 1
    else:
        return Fib(n-1) + Fib (n-2)

my_list = []
for i in range (-1*n, n+1):
    if (i < 0):
        my_list.append(FibNega(i))
    if (i > 0):
        my_list.append(Fib(i))
    if (i == 0):
        my_list.append(0)
    
print (my_list)                            