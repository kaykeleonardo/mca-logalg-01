escudo_ativo = False

n = int(input("Digite '1' para levantar o escudo, '0' para abaixar: "))
if n == 1:
    escudo_ativo = True
elif n == 0:
    escudo_ativo = False

if not(escudo_ativo):
    print("O escudo está abaixado, o cavaleiro tomou dano.")
else:
    print("O escudo está levantado, o cavaleiro não tomou dano.")