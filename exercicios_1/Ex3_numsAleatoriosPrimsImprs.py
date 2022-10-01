"""
Complete o programa

Pergunte ao utilizador qual é o intervalo para obter numeros aleatórios
Pergunte se deseja ver apenas pares, apenas impares ou apenas primos
Mostre todos os números aleatórios
Mostre todos os números que satisfazem o pedido do utilizador
"""
import random


def divisores(num):
    zeros = 0
    for j in range(1, num + 1):
        if num % j == 0:
            zeros += 1
    return zeros


def get_random(ini, fim):
    """
    Esta função devolve um número aleatório entre ini e fim inclusive
    :param ini: inicío do intervalo
    :param fim: fim do intervalo
    :return: número aleatório
    """
    return random.randrange(ini, fim + 1)


if __name__ == '__main__':
    numeros = list()
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    ver = input('1 - Pares, 2 - Impares, 3 - Primos')

    pares = list()
    impares = list()
    primos = list()

    for n in range(inicio, fim + 1):
        numeros.append(get_random(inicio, fim))

    print(numeros)

    for x in range(0, fim + 1):
        if numeros[x] % 2 == 0:
            pares.append(numeros[x])
        else:
            impares.append(numeros[x])

        if divisores(numeros[x]) == 2:
            primos.append(numeros[x])

    if ver == '1':
        print(f'Pares: {pares}')
    if ver == '2':
        print(f'Impares: {impares}')
    if ver == '3':
        print(f'Primos: {primos}')