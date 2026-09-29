com_conexao = True

n = int(input("Digite '1' se tem conexão, '0' se não possui conexão: "))
if n == 0:
    com_conexao = False

if not com_conexao:
    print("Modo Offline ativado. Executando músicas baixadas.")