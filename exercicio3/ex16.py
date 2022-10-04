'''
16. Escreva um programa que lê um número e cria uma capicua cuja primeira
metade é o número lido. Por exemplo:
Escreva um número
-> 347
347743
'''

if __name__ == '__main__':
    num = str(input('Introduza um número: '))
    nInvertido = ''
    for j in range(len(num)):
        nInvertido = num[j] + nInvertido
    nNum = num + nInvertido
    print(nNum)
