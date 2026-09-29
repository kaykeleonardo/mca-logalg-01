eh_noite = False
farol_ligado = False

n = int(input("Digite '1' para ligar o farol, '0' para desligar: "))
x = int(input("Digite '1' para noite, '0' para dia: "))

if n == 1:
    farol_ligado = True
if x == 1:
    eh_noite = True

if not farol_ligado and eh_noite:
    print("Atenção: Acenda os faróis para sua segurança!")