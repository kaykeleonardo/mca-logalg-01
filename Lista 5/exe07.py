largura = float(input('Largura (m): '))
altura = float(input('Altura (m): '))
mQuadrado = largura * altura
qtdTinta = mQuadrado / 3

print(f'''Tamanho área (m2): {mQuadrado:.2f}
Quantidade tinta necessaria (L): {qtdTinta}''')