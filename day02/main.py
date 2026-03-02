nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
print(f"Olá, {nome}! Você tem {idade} anos.")

print("Agora vamos fazer operações matemáticas!")
numero01 = float(input("Digite um número: "))
numero02 = float(input("Digite outro número: "))
sinal = input("Digite um sinal de operação (+, -, *, /): ")

if sinal == "+":
    print(numero01 + numero02)    
elif sinal == "-":
    print(numero01 - numero02)
elif sinal == "*":      
    print(numero01 * numero02)
elif sinal == "/":
    print(numero01 / numero02)
else:   
    print("Sinal de operação inválido.")

x =str(22)
print(type(x))
y = float(x)
print(type(y))
