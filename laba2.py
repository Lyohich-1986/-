import math
def problem_1(a, b):
    while a>=b:
        a=a-b
    return a
def problem_2(x, n):
    c = 0
    for i in range(1, n+1):
        c+=(x**i)/math.factorial(i)
    return c
def problem_3():
    a = 2*math.pi/6
    v0 = 35/3.6
    g = 9.81
    return 2*(v0**2)*(math.cos(a)**2)*math.tan(a)/g
def zaputyie(x):
    x = str(x).split('.')
    return len(x[1])
print('введите числа a, b большие нуля. a должно быть больше b')
while True:
    try:
        a = float(input('a = '))
        b = float(input('b = '))
        if a>b>0:
            break
        print('введите другие числа')
    except ValueError:
        print('введите другое число')
print( f'длина незанятой части а: {round(problem_1(a, b), max(zaputyie(a), zaputyie(b)))}')

print('введите вещественное x и натуральное n')
while True:
    try:
        x = float(input('x = '))
        n = int(input())
        if n > 0:
            break 
        print('введите новые числа')
    except ValueError:
        print('введите новые числа')
print(f'итог работы программы {problem_2(x, n)}')

print(f'Ответ на задачу по физике: {problem_3()}')
