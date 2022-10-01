'''
Complete o programa

Pergunte ao utilizador qual é o intervalo para obter numeros aleatórios
Pergunte se deseja ver todos o números, apenas pares, apenas impares ou
    penas primos.
Mostre todos os números aleatórios
Mostre todos os números que satifazes o pedido do utilizador
'''

import random
def get_random(ini, fim):
    '''
    Esta função devolve um numero aleatorio entre ini e fim incusive
    :param ini:
    :param fim:
    :return:
    '''
    return random.randrange(ini, fim +1)

