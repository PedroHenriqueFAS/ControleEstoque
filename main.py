estoque = {}

def adicionar_item(estoque, item, quantidade):
    if item in estoque:
        estoque[item] += quantidade
    else:
        estoque[item] = quantidade
    print(f'{quantidade} unidade(s) do produto {item} adicionada(s) ao estoque.')

def buscar_item(estoque, item):
    if item in estoque:
        return f'O estoque possui {estoque[item]} unidade(s) do produto {item}'
    else:
        return f'O produto {item} não está cadstrado no estoque.'

def checar_ocupacao(estoque):
    for chave, valor in estoque.items():
        print(f'{chave} : {valor} unidade(s)')

while True:
    print('Deseja continuar? (s/n)', end=' ')
    decisao = input()
    if decisao == 'n':
        break
    else:
        print('Pressione 1 para adicionar item ao estoque')
        print('Pressione 2 para buscar item no estoque')
        print('Pressione 3 para checar ocupação do estoque\n')
        print('Digite ', end = ' ')
        
        op = int(input())
        
        if op == 1:
            print('Digite o nome do Item e a quantidade a ser adicionado:', end=' ')
            item,qtd = input().split()
            qtd = int(qtd)
            adicionar_item(estoque, item, qtd) #a quantidade é convertida para inteiro e virou qtd
        elif op == 2:
            print('Digite o nome do Item a ser buscado: ')
            item = input()
            r = buscar_item(estoque, item)
            print(r)
        elif op == 3:
            checar_ocupacao(estoque)
        else:
            print('Opção {op} inválida! Digite novamente.')
            continue

print('Estoque finalizado!')