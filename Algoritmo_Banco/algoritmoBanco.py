fundo = input("Digite o nome do fundo: ")
taxa = float(input("Valor taxa: "))
teto = 13.0
risco = False

print(f'''\nNome do fundo: {fundo}
Valor da taxa: {taxa:.2f}%
Teto regulatório: {teto:.2f}%''')

print()

if taxa > teto:
  risco = True
  print("Alerta crítico !!! \n*Taxa incompatível*")
else:
  print("Taxa dentro das normas, pode proseguir.")

print()

if risco == True:
  print("Parecer do Auditor: Ativo bloqueado para novas emissões.")
else:
  print("Parecer do Auditor: Ativo liberado para comercialização.")