def lin_tex(msg):
    print("-" * 30)
    print(msg)
    print("-" * 30)


def lin():
    print("-" * 30)


def area(a, b):
    s = a * b
    print(f'A área de um terreno {a}x{b} é de {s}m².')


lin_tex('Controle de Terrero')
a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
lin()
area(a, b)