import random

def problem1(n):
    c = [[random.uniform(-100, 100) for i in range(n)] for j in range(n)]
    m, k = [], []
    for i in range(n):
        for j in range(n):
            if j > i:
                m.append(c[i][j])
            else:
                k.append(c[i][j])
    return m, k

def problem2(n):
    person = {
       "имя": input("Введите имя: "),
       "пол": input("Введите пол: "),
       "индивидуальный номер": input("Введите индивидуальный номер: ")
   }
    while True:
    try:
        age = int(input("Введите возраст: "))
        if age < 0:
            print("Возраст не может быть отрицательным!")
            continue
        person["возраст"] = age
        break
    except ValueError:
        print("Ошибка! Введите число.")
    for k in person:
        print(k, ':', person[k])
#main()
