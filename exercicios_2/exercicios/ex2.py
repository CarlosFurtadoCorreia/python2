def opc_for(num1, num2):
    soma = 0
    for x in range(num1, num2 + 1):
        soma += x
        #print(soma)
    return soma


def opc_while(num1, num2):
    soma = 0
    x = 0
    while x < (num2 - num1) + 1:
        soma += num1 + x
        x += 1
        #print(soma)
    return soma

if __name__ == '__main__':
    continuar = 's'
    while continuar == 's':
        prim_num = int(input('Introduza o primeiro número: '))
        seg_num = int(input('Introduza o segundo número: '))
        opcao = input('Pretende utilizar "while" ou "for"? ')
        while True:
            if opcao == 'for':
                print(opc_for(prim_num, seg_num))
                break
            elif opcao == 'while':
                print(opc_while(prim_num, seg_num))
                break
        continuar = input('Pretende repetir? [s] ou [n]? ')
    print(f'Adeus!')