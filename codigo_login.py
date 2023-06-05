usuarios = []  

while True:
    print("\nEscolha uma opção:")
    print("1 - Registrar")
    print("2 - Login")
    print("3 - Sair")
    escolha = input("Opção: ")

    if escolha == "1":
        nome = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")
        usuarios.append({"nome": nome, "senha": senha})  
        print("Usuário registrado com sucesso!")

    elif escolha == "2":
        nome = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")
        for usuario in usuarios:
            if usuario["nome"] == nome and usuario["senha"] == senha:
                print("Login bem sucedido!")
                break
        else:
            print("Nome de usuário ou senha incorretos!")

    elif escolha == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida! Tente novamente.")