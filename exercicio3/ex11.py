'''
11. Escreva um programa em Python que lê um número inteiro positivo e
produz o número correspondente a inverter a ordem dos seus dígitos. Por
exemplo,
'''

def lernumero():
    while True:
        try:
            numero = int(input('Introduza um número: '))
            break
        except ValueError:
            print('Introduza um número válido.')
    return numero

if __name__ == '__main__':
    num = lernumero()
    numstr = str(num)
    base = 1
    gerado = 0

    '''for j in range(len(numstr)):
        if int(numstr[len(numstr) - j - 1]) % 2 != 0:
            print(numstr[len(numstr) - j - 1])
            gerado += int(numstr[len(numstr) - j - 1]) * base
            base *= 10
    print(gerado)'''

    ns = []
    for j in str(num):
        if int(j) % 2 != 0:
            ns.append(j)
    print(int(''.join(ns)))
