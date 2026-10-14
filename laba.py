def problem_1(x):
    return x**2//2
def problem_2(a):
    if float(a[0])>0 and float(a[1])>0:
        return('I')
    if float(a[0])<0 and float(a[1])>0:
        return('II')
    if float(a[0])<0 and float(a[1])<0:
        return('III')
    if float(a[0])>0 and float(a[1])<0:
        return('IV')

print(problem_1(int(input('ВВЕДИТЕ ВАШЕ ЧИСЛО: '))))
print(problem_2(input('ВВЕДИТЕ ВАШИ ЧИСЛА: ').split()))
