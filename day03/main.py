nome = input("Digite seu nome: ")
password = input("Digite sua senha de admin: ")

user ={
    'Jorge': 'jorge123',
    'Maria': 'maria123',
}

if nome in user and user[nome] == password:
    print(f"Bem-vindo, {nome}!")
else:
    print("Acesso negado. Nome ou senha incorretos.")