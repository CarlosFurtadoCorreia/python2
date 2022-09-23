'''
Inserir os números pares entre 1 e o número inserido
'''

# range(start, stop, step)

from programa3 import par

if __name__ == '__main__':
    num1 = int(input('Insira o primeiro número: '))
    #num2 = int(input('Insira o segundo número: '))

    for x in range(1, num1 + 1):
        if par(x):
            print(x)
