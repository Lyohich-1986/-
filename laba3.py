def problem_1(a):
    result = ""
    dive = 0
    for symbols in a:
        if symbols == '(':
            result += symbols
            dive += 1
        elif symbols == ')':
            result += symbols
            if dive > 0:
                dive -= 1
        elif dive == 0:
                result += symbols   
    return result

def problem_2(a):
    words = []
    for i in a:
        cnt = 0
        for j in i:
            if j == 'a' or j == 'A' or j == 'а' or j == 'А':
                cnt+=1
            if cnt == 2:
                break
        if cnt>=2:
            words.append(i)
    return words

def problem_3(a):
    for i in range(len(a)):
        if type(a[i]) != int and type(a[i]) != float:
            print("В массиве не число")
            return None, None
    mx, mxn = a[0], 0
    for i in range(len(a)):
        if abs(a[i]) > abs(mx):
            mx = a[i]
            mxn = i
    j = 0
    while j < len(a) and a[j] <= 0:
        j += 1
    sum_plus = 0
    if j < len(a):
        for i in range(j + 1, len(a)):
            sum_plus += a[i]
    return mxn, sum_plus
    
a = input('Введите непустую строку: ')
while len(a)==0:
    a = input('Введите НЕПУСТУЮ строку: ')
print(f'Исходная строка: {a}')
print(f'строка без чисел меж скобками: {problem_1(a)}')

words = []
print("Вводите слова по одному (Enter на пустой строке – завершить ввод).")
while True:
    word = input("Слово: ")
    if len(word) == 0:
        break
    has_space = False
    for ch in word:
        if ch == ' ':
            has_space = True
            break
    if has_space:
        print("Ошибка: слово не может содержать пробел. Повторите ввод.")
        continue
    words.append(word)
if len(words) == 0:
    print("Вы не ввели ни одного слова.")
else:
    print(f"Исходный массив слов: {words}")
    print(f"Слова с двумя и более буквами 'а': {problem_2(words)}")

a = []
print("Вводите числа по одному (Enter на пустой строке — завершить ввод).")
while True:
    s = input("Число: ")
    if len(s) == 0:
        break
    try:
        x = float(s)
    except ValueError:
        print("Ошибка: введите число.")
        continue
    if x == int(x):
        x = int(x)
    a.append(x)
if len(a) == 0:
    print("Вы не ввели ни одного числа.")
else:
    print(f"Исходный список: {a}")
    mxn, total = problem_3(a)
    print(f"Номер максимального по модулю элемента: {mxn + 1}")
    print(f"Сумма элементов после первого положительного: {total}")
    
