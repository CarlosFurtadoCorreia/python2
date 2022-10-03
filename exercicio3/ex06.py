'''
6. Escreva um programa em Python que lê três números e que diz qual o
maior dos números lidos.
'''

if __name__ == '__main__':
    nums = ['primeiro número', 'segundo número', 'terceiro número']
    num = []
    nMaior = 0
    nMenor = 0
    for j in range(len(nums)):
        num.append(int(input(f'Introduza o {nums[j]}: ')))
        if j == 0:
            nMaior = nMenor = num[j]
        else:
            if num[j] > nMaior:
                nMaior = num[j]
            if num[j] < nMenor:
                nMenor = num[j]
    print(nMaior)
