materia = 3.5
maoObra = 1.5
embalagem = 0.8

capinhas = int(input('Quantidade capinhas produzidas: '))
preco = float(input('Valor de venda: R$'))

producao = (materia + maoObra + embalagem) * capinhas
lucro = (preco * capinhas) - producao

print(f'''Valor total: R${preco * capinhas:.2f}
Custo Produção: R${producao:.2f}
Lucro: R${lucro:.2f}''')