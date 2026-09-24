distancia = float(input('Distancia Percorrida (km): '))
tempo = float(input('Tempo Gasto (min): '))

velocidade = distancia / (tempo / 60) 

print(f'Velocidade km/h: {velocidade:.2f}')