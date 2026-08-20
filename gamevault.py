print("========================")
print("       GAMEVAULT")
print("========================")

print("1 - Adicionar jogo")
print("2 - Listar jogos")
print("3 - Sair")

escolha = int(input("escolha o que quer "))

while escolha > 3 or escolha < 1:
    print("error 402")
    escolha = int(input("(opção não identificada escolha novamente ou saia.)"))

if escolha == 1:
    print("Adicionando jogo...")
elif escolha == 2:
    print("Listando jogos...")
else:
    print("Saindo...")