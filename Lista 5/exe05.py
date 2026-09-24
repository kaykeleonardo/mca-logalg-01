segundos = int(input('Segundos: '))

horas = segundos // 3600

resto_segundos = segundos % 3600
minutos = resto_segundos // 60

segundos = resto_segundos % 60

print(f"{horas}h {minutos}m {segundos}s")
