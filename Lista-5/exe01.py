cura = 15
energia = 25

qtdCura = int(input('Quantidade poções de Cura: '))
qtdEnergia = int(input('Quantidade poções de Energia: '))

mana = (cura * qtdCura) + (energia * qtdEnergia)

print(f'Total Mana = {mana}')
