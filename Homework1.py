print ('1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, ')
print (f'является ли этот день выходным.\n')

day = int(input ('введите день недели: '))
while (day < 1 or day > 7 ):
    day = int(input ('введите день недели от 1 до 7: ')) 
print (f'день недели {day} выходной? - ', end = ' ' )
if ( day == 6 or day == 7):
    print ('yes')
else:
    print ('no')
input()





print ('2. Напишите программу для. проверки истинности')
print (f'утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.\n')

x = 0
y = 0
z = 0
count = 0
for i in range (1,9):
    if (not(x == 1 or y == 1 or z == 1) == ( not x == 1 and not y == 1 and not z == 1)):
        count += 1
    else:
        break
    if (i == 1):
        x = 0
        y = 0
        z = 1
    elif (i == 2):
        x = 0
        y = 1
        z = 0
    elif (i == 3):
        x = 0
        y = 1
        z = 1   
    elif (i == 4):
        x = 1
        y = 0
        z = 0
    elif (i == 5):
        x = 1
        y = 0
        z = 1
    elif (i == 6):
        x = 1
        y = 1
        z = 0
    else:
        x = 1
        y = 1
        z = 1
if count == 8: 
    print ('логическое выражение истинно')
else:
   print ('логическое выражение не истинно')
input()



print ('3. Напишите программу, которая принимает на вход координаты точки (X,Y), причем X!=0 и Y!=0')
print (f'и выдает номер четверти плоскости \n ')

X = int(input ('введите абсциссу Х: '))
Y = int(input ('введите ординату Y: '))

while (X == 0 or Y == 0 ):
    print (' X или Y не должны равнятся 0, введите корректные данные: ')
    X = int(input ('введите абсциссу Х: '))
    Y = int(input ('введите ординату Y: '))   
if (X > 0 and Y > 0):
    print (f'точка [{X},{Y}] лежит в 1 четверти')
elif (X < 0 and Y > 0):
    print (f'точка [{X},{Y}] лежит в 2 четверти')
elif (X < 0 and Y < 0):
    print (f'точка [{X},{Y}] лежит в 3 четверти')
else:
    print (f'точка [{X},{Y}] лежит в 4 четверти')
input()


print ('4. Напишите программу, которая по заданному номеру четверти')
print (f'показывает диапозон возможных координат точек в этой четвенрти (x и y)\n')

num_plan_coord = int(input ('введите номер четиверти кординатной плоскости: '))
if (num_plan_coord == 1):
    print (f'диапазон в четверти {num_plan_coord}: x=[0, n]; y = [0, n]')
elif (num_plan_coord == 2):
    print (f'диапазон в четверти {num_plan_coord}: x=[0, -n]; y = [0, n]')
elif (num_plan_coord == 3):
    print (f'диапазон в четверти {num_plan_coord}: x=[0, -n];1 y = [0, -n]')
elif (num_plan_coord == 4):
    print (f'диапазон в четверти {num_plan_coord}: x=[0, n]; y = [0, -n]')
else:
    print ('некорректные данные, повторите ввод')

input()




print ('5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние')
print (f'между ними в 2D пространстве \n ')

import random
Ax = random.randint(-10,10)
Ay = random.randint(-10,10)
Bx = random.randint(-10,10)
By = random.randint(-10,10)
AB = round((((abs(Ax - Bx)**2 + abs(Ay - By)**2))**0.5), 2)
print (f'расстояние от т.А [{Ax},{Ay}] до т.В [{Bx},{By}] => AB = {AB}')
