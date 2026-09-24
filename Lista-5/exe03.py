peso = float(input('Digite o peso do saco de ração (Kg): '))
consumo = float(input('Digite o valor consumido pelo cão (g): '))

consumoSemana = consumo * 5
pesoG = peso * 1000

total = pesoG - consumoSemana

print(f'Total de ração restante após 5 dias: {total:.2f} gramas')


