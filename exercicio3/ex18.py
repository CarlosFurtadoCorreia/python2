'''18. Escreva um programa que lê um número inteiro e determina quantas vezes
aparecem dois zeros seguidos. Por exemplo:
Escreva um inteiro
? 98007640003
O numero tem 3 zeros seguidos'''

def cZeros(num):
    count = 0
    while num % 10 == 0:
        count += 1
        num /= 10
    return count

if __name__ == '__main__':
    while True:
        try:
            num = int(input('Digite o número inicial: '))
            print(f'O {num} introduzido tem {cZeros(num)} zeros seguidos.')
            continuar = input('Pretende repetir [s] ou [n]? ')
            if continuar == 'n':
                break
        except ValueError:
            print('Introduza um número válido.')
