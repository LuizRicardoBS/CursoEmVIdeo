import time


def lin():
    print('-=' *30)


def tempo():
    time.sleep(0.5)


def Contador():
    lin()
    pos = 1
    até = 10
    print('Contagem de 1 até 10 de 1 em 1')
    tempo()
    while pos <= até:
        print(pos, end=' ')
        tempo()
        pos += 1
    tempo()
    print('FIM')
    tempo()
    lin()
    pos = 10
    até = 1
    tempo()
    print('Agora de 10 até 0 de 2 em 2')
    tempo()
    while pos >= até:
        print(pos, end=' ')
        tempo()
        pos += -2
    tempo()
    print('FIM')
    tempo()
    lin()

    print('Agora é a sua vez de personalizar a contagem!')
    início = int(input('Início: '))
    fim = int(input('Fim: '))
    try:
        passo = int(input('Passo: '))
    except ValueError:
        passo = 1


    if passo == 0 or passo == '':
        passo = 1
        print(f'Contagem de {início} até {fim} de {passo} em {passo}')
        if início < fim:
            while início <= fim:
                print(início, end=' ')
                tempo()
                início += passo
            tempo()
            print('FIM')
        elif início > fim:
            while início >= fim:
                print(início, end=' ')
                tempo()
                início += passo
            tempo()
            print('FIM')
    else:
        if início < fim:
            while início <= fim:
                print(início, end=' ')
                tempo()
                início += passo
            tempo()
            print('FIM')
        elif início > fim:
            while início >= fim:
                print(início, end=' ')
                tempo()
                início += passo
            tempo()
            print('FIM')


Contador()
