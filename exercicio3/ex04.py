'''
4. Escreva um programa que lê um número inteiro correspondente a um
certo número de segundos e que escreve o número de dias, horas, minutos
e segundos correspondentes a esse número. Por exemplo,

Escreva o número de segundos 345678
dias: 4 horas: 0 mins: 1 segs: 18
'''

num = int(input('Introduza um número em segundos: '))
dias = num / 86400
horas = dias / 24
minutos = horas / 60
segundos = minutos * 60

print(f'Corresponde a {dias:.5f} dias, {horas:.5f} horas, {minutos:.5f} minutos, {segundos:.5f} segundos.')