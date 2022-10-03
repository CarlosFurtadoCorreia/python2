'''
2. Escreva um programa em Python que lê valores correspondentes a uma
distância percorrida (em Km) e o tempo necessário para a percorrer (em
minutos), e calcula a velocidade média em:
(a) Km / h
(b) m/s
'''

if __name__ == '__main__':
    num = int(input('Introduza a sua distancia em kms: '))
    num2 = int(input('Introduza o tempo em minutos: '))
    mts = num * 1000
    horas = num2 / 60
    print(f'Média em km/h: {num / horas}')
    segundos = horas / 60
    print(f'Média em m/s: {mts * segundos :.2f}')

    '''opc = input('Selecione uma das opções:\n'
                '[1] - Km / h\n'
                '[2] - m/s\n')'''
    '''if opc == '1':
        print(f'{media_km:.2f}')
    elif opc == '2':
        print(f'{media_mts}')'''

