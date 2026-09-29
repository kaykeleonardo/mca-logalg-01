aceitou_termos = False

n = int(input("Digite '1' para aceitar os termos, '0' para não aceitar: "))
if n == 1:
    aceitou_termos = True
elif n == 0:
    aceitou_termos = False

if not aceitou_termos:
    print("Você não aceitou os termos, acesso negado. \nAceite os termos para jogar.")
else:
    print("Você aceitou os termos, acesso permitido.")