jogos = []

while True:
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

        nome = input("Qual o nome do jogo? ")
        plataforma = input("plataforma? ")
        nota = input("nota: ")

        print(
            nome,
            "//nota:",
            nota,
            "//plataforma jogavel:",
            plataforma
        )

        print("cadastrando jogo.....")

        jogo = {
            "nome": nome,
            "nota": nota,
            "plataforma": plataforma
        }

        jogos.append(jogo)

    elif escolha == 2:
        print("Listando jogos...")

        for jogo in jogos:
            print("========================")
            print("Nome:", jogo["nome"])
            print("Plataforma:", jogo["plataforma"])
            print("Nota:", jogo["nota"])

    else:
        print("Saindo...")
        break
