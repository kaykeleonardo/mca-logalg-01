cofre_trancado = False

n = int(input("Digite '1' para trancar o cofre, '0' para destrancar: "))
if n == 1:
    cofre_trancado = True
elif n == 0:
    cofre_trancado = False

if not cofre_trancado:
    print("Alerta o cofre está destrancado.")
else:
    print("O cofre está trancado.")