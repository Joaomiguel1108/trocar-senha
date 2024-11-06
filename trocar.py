import random


tentativas = 5
tentativas2 = 5
email1 = "a" 
esqueceu = 0 
senha1 = "macaco123"
trocar = 0
tentativas3 = 0



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

if esqueceu == "sim":
    
    
    print("um codigo de verificação foi enviado no seu email")
    print(numeros)
    receba = str(input("Você recebeu o código?"))
    
if receba == "sim":
    codigo = int(input("Digite o codigo"))
    
elif codigo == 1234 and codigo == 4321 and codigo == 4444 and codigo == 1357 :
    trocar = input("Digite uma nova senha")
    senha1 = trocar
    
while trocar == senha1:
    
    senha2 = (input("Digite sua senha novamente"))
    
    if senha2 == trocar:
        print("Senha correta")
        break
    else:
        tentativas3 -= 1
        print("Senha incorreta")
        esqueceu = str(input("esqueceu sua senha novamente?"))


        


if tentativas == 0:
    print("Acesso bloqueado, tente novamente mais tarde")
        
