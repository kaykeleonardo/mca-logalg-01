tanque_reserva = False

n = int(input("Digite '1' se o tanque estiver na reserva: "))
if n == 1:
    tanque_reserva = True

if not tanque_reserva:
    print("Decolagem autorizada! Sistemas em perfeito estado.")