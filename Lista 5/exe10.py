moedas = int(input('Quantidade Moedas: '))
exploradores = int(input('Quantidade Exploradores: '))
divisor = moedas / exploradores
resto = moedas % exploradores


print(f'''Moedas Exploradores: {divisor}
Bonus lider: {resto}''')
