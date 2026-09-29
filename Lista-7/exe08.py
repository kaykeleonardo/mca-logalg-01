obstaculo_detectado = False

n = int(input("Digite '1' se houver obstáculo no caminho do portão, '0' se não houver: "))
if n == 1:
    obstaculo_detectado = True

if not obstaculo_detectado:
    print("Portão abrindo com segurança.")
else:
    print("Atenção: Obstáculo detectado! Portão não pode ser aberto.")