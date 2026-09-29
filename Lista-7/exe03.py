solo_umido = False

n = int(input("Digite '1' para solo umido, ou '0' para solo seco: " ))

if n == 1:
    solo_umido = True
elif n == 2:
    solo_umido = False

if not solo_umido:
    print("Irrigadores ligados: umidade abaixo do ideal.")
else:
    print("Irrigadores desligados.")