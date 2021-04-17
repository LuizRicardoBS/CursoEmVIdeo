def Contator(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')


def Contador2(*nuh):
    Tam = len(nuh)
    print(Tam)


Contator(2, 1, 7)
Contator(8, 0,)
Contator(4, 4, 7, 6, 2)