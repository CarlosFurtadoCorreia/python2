'''inserir valores para vendas
total de vendas de gasolina
total de venda de gasoleo
total de vendas para cada ilha
total de vendas de combustivel
quais ilhas venderam mais
quais ilhas venderam menos
qual é ilha consumiu mais gasolina
qual ilha consumiu mais gasoleo'''

ilhas = ['Terceira', 'Pico', 'Faial', 'São Jorge', 'Graciosa', 'Flores', 'Corvo']
tipos = ['Gasolina', 'Gasóleo']
vendas = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

totais = [0, 0, 0, 0, 0, 0, 0]

if __name__ == '__main__':
    # Obter input
    for x in range(len(vendas)):
        for y in range(len(vendas[x])):
            while True:
                try:
                    vendas[x][y] = int(input(f'Insira vendas de {tipos[x]} para a ilha {ilhas[y]}: '))
                    break
                except ValueError:
                    print(f'Insira um valor válido para vendas de {tipos[x]} na ilha {ilhas[y]}')
    for venda in vendas:
        print(venda)

    # Imprimir vendas por tipo
    for x in range(len(vendas)):
        total = 0
        for y in range(len(vendas[x])):
            total += vendas[x][y]
        print(f'Total de vendas para {tipos[x]} = {total}')

    # Imprimir vendas por ilha
    z = 0
    for y in range(len(vendas[z])):
        z += 1
        total = 0
        for x in range(len(vendas)):
            total += vendas[x][y]
        print(f'Total de vendas para {ilhas[y]} = {total}')
        totais[y] = total

    # Imprimir o total de vendas de combustível
    total_combustivel = 0
    for y in range(len(vendas)):
        for x in range(len(vendas)):
            total_combustivel += vendas[x][y]
    print(f'Total de vendas de combustivel nos Açores: {total_combustivel}')

    #Imprimir quais ilhas venderam mais
    venda_maior = totais[0]
    venda_menor = totais[0]
    for y in range(1, len(totais)):
        if totais[x] > venda_maior:
            venda_maior = totais[x]
        if totais[x] < venda_menor:
            venda_menor = totais[x]

    ilhas_maior = []
    ilhas_menor = []

    for x in range(len(totais)):
        if totais[x] == venda_maior:
            ilhas_maior.append(ilhas[x])
        if totais[x] == venda_menor:
            ilhas_menor.append(ilhas[x])

    print(totais)
    print(f'Ilhas maior: {ilhas_maior} = {venda_maior}')
    print(f'Ilhas menor: {ilhas_menor} = {venda_menor}')