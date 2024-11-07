import random

receba = 0
tentativas = 5
tentativas2 = 5
email1 = "a" 
esqueceu = 0 
senha1 = "macaco123"
trocar = []
tentativas3 = 0

print(senha1)

verificado = ["1234", "4321", "1357", "4444"]
numeros = random.choice(verificado)

while tentativas2 > 0:
    email = str(input("Digite seu email")) 
    if email == email1:
        print("Email correto")
        break
        
while tentativas > 0 and esqueceu != "sim":
    
    senha = (input("Digite sua senha"))
    
    if senha == senha1:
        print("Senha correta")
        break

    
    else:
        tentativas -= 1
        print("Senha incorreta")
        esqueceu = str(input("esqueceu sua senha?"))

while esqueceu == "sim":
    
    print("um codigo de verificação foi enviado no seu email")
    print(numeros)
    receba = str(input("Você recebeu o código?"))
    if receba == "sim":
        break
    
while receba == "sim":
    codigo = int(input("Digite o codigo"))
    if codigo == 1234:
        trocar = input("Digite uma nova senha")
        senha1 = trocar
        break
    elif codigo == 4444:
        trocar = input("Digite uma nova senha")
        senha1 = trocar
        break
    elif codigo == 4321:
        trocar = input("Digite uma nova senha")
        senha1 = trocar
        break
    elif codigo == 1357:
        trocar = input("Digite uma nova senha")
        senha1 = trocar
        print(senha1)
        
        break
while senha1 == trocar:
    print(senha1)
    senha2 = (input("Digite sua senha novamente"))
    
    
    if senha2 == senha1:
        print("Senha correta")
        break
    else:
        tentativas3 -= 1
        print("Senha incorreta")
        esqueceu = str(input("esqueceu sua senha novamente? burro"))


        


if tentativas == 0:
    print("Acesso bloqueado, tente novamente mais tarde")
        
