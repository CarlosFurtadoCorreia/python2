'''lista com 5 nums
lista tem que gerar nums entre 1-50
'''

#GERAR NUMS ALEATORIOS
import random


def get_random(ini, fim):
    """
    Esta função devolve um número aleatório entre ini e fim inclusive
    :param ini: inicío do intervalo
    :param fim: fim do intervalo
    :return: número aleatório
    """
    return random.randrange(ini, fim + 1)

if __name__ == '__main__':
    nums = [0, 0, 0, 0, 0]
    estrelas = [0, 0]
    jogos = [0, 0, 0, 0, 0]
    for x in range(len(nums)):
        while True:
            numero = get_random(1, 50)
            if numero not in nums:
                nums[x] = numero
                break
    print(f'5 números: {nums}')

    for x in range(len(estrelas)):
        while True:
            numero = get_random(1, 12)
            if numero not in estrelas:
                estrelas[x] = numero
                break
    print(f'Estrelas: {estrelas}')

    troquei = True
    x = 0
    while troquei:
        troquei = False
        for x in range(4):
            if nums[x] > nums[x + 1]:
                troquei = True
        print(nums)
