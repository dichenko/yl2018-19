import sys

try:
    mas = []
    k = sorted(sys.argv[1:])

    f = open(k[-1])

    for el in f:
        mas.append(el.strip())

    if '--sort' in sys.argv:
        mas = sorted(mas)

    if '--num' in sys.argv:
        for i in range(len(mas)):
            mas[i] = (str(i) + ' ' + mas[i])

    if '--count' in sys.argv:
        n = len(mas)
        mas.append('rows count: ' + str(n))
    for el in mas:
        print(el)

    f.close()

except Exception:
    print('ERROR')
