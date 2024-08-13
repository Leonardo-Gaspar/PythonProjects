x = ['1.0', 10, "100", 1000.0]
y = ['soma', 'subtração', 'multiplicação', 'divisão']

for i in x:
    n = 2
    z= y.pop(0)

    if z == 'soma':
        print(i + str(n))
    elif z == 'subtração':
        print(i - n)
    elif z == 'multiplicação':
        print(i * n)
    else:
        print(i/n)