"""
Declare uma lista para guardar as vendas de gasolina e gas´´eo no grupo oriental
Apresente:
- Total das vendas
- O total de vendas de gasolina
- O total de vendas de gasóleo
- O total de vendas para cada ilha
Exemplo da estrutura de armazenamento das vendas:
    vendas = [
         TER PIC  FAI  GRA  SJR
        [10, 20 , 30, 40 , 50], #Gasolina
        [15, 25, 35, 45, 55]    #Gasoleo
    ]
    ou então:
    vendas = [
         Gasoleo
          |  Gasolina
        [10, 15], TER
        [20, 25], PIC
        [30, 35], FAI
        [40, 45], GRA
        [50, 55]  SJR
    ]
"""

if __name__ == '__main__':
    vendas = [
        [10, 20, 30, 40, 50],  # Gasolina
        [15, 25, 35, 45, 55]  # Gasoleo
    ]

    print(vendas)

    # para mostrar cada lista separadamente
    for venda in vendas:
        print(venda)
        # mostrar cada valor de cada lista individualmente
        for v in venda:
            print(v)

    x = 0
    y = 0

    # mostrar valor da lista pretentido utilizando as variaveis x e y
    print(f'vendas[x][y]: {vendas[x][y]}')
    for x in range(5):
        total_vendas = 0
        for y in range(2):
            print(f'vendas [{y}] [{x}] = {vendas[y][x]}')
        total_vendas = total_vendas + vendas[y][x]
        print(f'Total de vendas: {total_vendas}')
        print('================')
        
    '''for x in range(len(vendas)): #identico ao tamanho da lista (2)
        for y in range(len(vendas[0])): #identico aos valores das casas da lista
            print(f'vendas [{x}] [{y}] = {vendas[x][y]}')
        print('xxxx')'''

    #total de vendas

    for x in range(5):
        total_linha = 0
        for y in range(2):
            print(f'vendas [{y}] [{x}] = {vendas[y][x]}')
            #total_vendas = total_vendas + vendas[y][x]
            total_linha = total_vendas + vendas[y][x]
        print(f'Total de linhas: {total_linha}')
        print('================')
    #print(f'Total de vendas: {total_vendas}')

    
