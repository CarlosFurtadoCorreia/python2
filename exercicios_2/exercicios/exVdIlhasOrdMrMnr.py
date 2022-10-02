ilhas = ['Terceira', 'Pico', 'Faial', 'Graciosa', 'S. Jorge']

if __name__ == '__main__':
    vendas = []
    vMaior = 0
    vMenor = 0
    vOrdenadas = []

    for j in range(len(ilhas)):
        vendas.append(int(input(f'{ilhas[j]}: ')))
        if j == 0:
            vMaior = vMenor = vendas[j]
        else:
            if vendas[j] > vMaior:
                vMaior = vendas[j]
            if vendas[j] < vMenor:
                vMenor = vendas[j]

        if j == 0 or vendas[j] > vOrdenadas[-1]:
            vOrdenadas.append(vendas[j])
        else:
            pos = 0
            while pos < len(vOrdenadas):
                if vendas[j] <= vOrdenadas[pos]:
                    vOrdenadas.insert(pos, vendas[j])
                    break
                pos += 1

    print(f'Vendas Ordenada: {vOrdenadas}')
    print(f'Menor: {vMenor}')
    print(f'Maior: {vMaior}')
    print(f'Vendas: {vendas}')
