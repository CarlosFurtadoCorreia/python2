'''
14. Escreva um programa que lê um inteiro e calcula a soma dos seus dígitos.
'''

def soma(n):
    num = 0
    for j in str(n):
        num += int(j)
    return num

if __name__ == '__main__':
    num = int(input(f'Introduza um número inteiro: '))
    print(soma(num))
