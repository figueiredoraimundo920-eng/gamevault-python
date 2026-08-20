print("========================")
print("       GAMEVAULT")
print("========================")

print("1 - Adicionar jogo")
print("2 - Listar jogos")
print("3 - Sair")

escolha = int(input(""))
while escolha > 3 or escolha < 1:
    print("error 402")
    escolha = int(input("(opção não identificada escolha novamente ou saia.)"))

if escolha == 1:
    print("Adicionando jogo...")
    while escolha != 3:
        if escolha == 1:
            nome = input("Qual o nome do jogo? ")
            plataforma = input("plataforma? ")
            nota = input("nota: ")
            print(nome, "//nota:", nota, "//plataforma jogavel:", plataforma)
            print("cadastrando jogo.....")
            nome2 = {}
            nome2['primeiro jogo'] = nome, '-', plataforma, '-', nota
            nome2.append(nome)

            if escolha == 3:
                print("saindo...")
            print("========================")
            print("       GAMEVAULT")
            print("========================")

            print("1 - Adicionar jogo")
            print("2 - Listar jogos")
            print("3 - Sair")
            escolha = int(input(""))

elif escolha == 2:
    print("Listando jogos...")
    while escolha != 3:
        if escolha == 2:
            def nome2():
                return nome2['primeiro jogo']
            nome2()
        if escolha == 3:
            print("saindo...")
        print("========================")
        print("       GAMEVAULT")
        print("========================")

        print("1 - Adicionar jogo")
        print("2 - Listar jogos")
        print("3 - Sair")
        escolha = int(input(""))

else:
    print("Saindo...")