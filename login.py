import getpass

nome = input("Digite o seu nome: ")
senha = getpass.getpass("Digite a sua senha: ")
senha_valida = "301155"
if senha == senha_valida:
    print(f"Bem-vindo, {nome}!")
else:
    print("Login ou senha inválida")
