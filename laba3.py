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
