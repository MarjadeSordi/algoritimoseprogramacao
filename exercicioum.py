##Exercicio 1:

produtos = ['calça', 'bermuda', 'camiseta', 'saia','blusa']
preco = [80, 50, 30, 60, 40]
quantidade = [10, 5, 8, 20, 6, 8]


def nome_produto(): 
 
  for i, produto in enumerate(produtos):
    print (i + 1, produto)
  produt = int(input('Escolha um produto pelo indice para consultar: '))
  product = produtos[(produt - 1)]
  quant = quantidade[(produt - 1)] 
  pre = preco[(produt - 1)]
  return print("Produto: ", product, 
  "Quantidade: ", quant, 
  "Preço: R$",pre)


def deletar_produto():
  for i, produto in enumerate(produtos):
    print (i + 1, produto)
  produt = int(input('Escolha um produto pelo indice para deletar:'))
  del produtos[(produt - 1)]
  del  quantidade[(produt - 1)]
  del preco[(produt - 1)]
  return print("Lista de produtos atualizada: ", produtos,
  "Lista de quantidades atualizada", quantidade ,
  "Lista de valores atualizada", preco)


def menu():
    while True:
        print('''Digite: 
        1- para consultar um produto, seu valor e quantidade;
        2- para deletar um produto
        0 - para sair''')
        consulta= input ('')
        if consulta == '0':break 
        elif consulta == '1': nome_produto()
        elif consulta == '2': deletar_produto()
        #if consulta == '3':
        #if consulta == '4':


menu()

    