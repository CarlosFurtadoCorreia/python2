'''
1. Escreva um programa em Python que pede ao utilizador que lhe forneça
dois números (x e y) e que escreve o valor de (x + 3 * y) * (x - y).
O seu programa deve gerar uma interação como a seguinte:
Vou pedir-lhe dois numeros
Escreva o primeiro numero, x = 5
Escreva o segundo numero, y = 6
O valor de (x + 3 * y) * (x - y) e: -23
'''

if __name__ == '__main__':
    num1 = int(input('Introduza um primeiro número: '))
    num2 = int(input('Introduza um segundo número: '))

    resultado = (num1 + 3 * num2) * (num1 - num2)

    print(f'O valor de (x + 3 * y) * (x - y) e: {resultado}')
    