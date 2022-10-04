'''
10. Escreva um programa em Python que lê um número inteiro positivo e
calcula o número obtido do número lido que apenas contém os seus dígitos
impares. Por exemplo,
Escreva um inteiro
? 785554
Resultado: 7555
'''

def impar(n1):
    n1 = int(n1)
    if n1 % 2 != 0:
        return n1
    else:
        return ''

if __name__ == '__main__':
    while True:
        try:
            num = int(input('Introduza um número inteiro positivo: '))
            if num < 0:
                print('Introduza um número positivo!')
                pass
            else:
                num = str(num)
                nImpar = ''
                for j in num:
                    nImpar += str(impar(j))
                break

        except ValueError:
            print('Introduza um número válido.')

    print(f'Resultado: {nImpar}')

