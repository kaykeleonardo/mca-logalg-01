mDez = int(input('Quantidade de Moedas de 10 centavos: '))
mVinte = int(input('Quantidade de Moedas de 25 centavos: '))
mCinquenta = int(input('Quantidade de Moedas de 50 centavos: '))

total = (mDez * 0.1) + (mVinte * 0.25) + (mCinquenta * 0.5)

print(f'Total guardado em R${total:.2f}')
