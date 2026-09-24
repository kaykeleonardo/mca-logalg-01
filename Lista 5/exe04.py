painel = 1.2

qtdPainel = int(input('Quantidades de Paineis: '))
valorCobrado = float(input('Valor cobrado por kWh: R$'))

geradoMes = qtdPainel * painel * 30
totalMes = valorCobrado * geradoMes

print(f'''Quantidade de kWh gerado no mês: kWh {geradoMes:.2f}
Quantidade economizado no mês: R${totalMes:.2f}''')