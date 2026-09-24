total = float(input('Digite o total arrecadado com as vendas: R$'))

guardado = total * 0.1
divisao = (total - guardado) / 3

print(f'''Total arrecadado: R${total:.2f}
Total Guardado: R${guardado:.2f}
Valor para cada amigo: R${divisao:.2f}''')

