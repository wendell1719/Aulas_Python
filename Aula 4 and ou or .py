# digite para entrar 
entrada = input(" [E] entrar [S] sair : ")
# variavel de senha criada 
senha_digitada = input("senha : ")
#senha para entrar 
senha_permitida = "12345"

# condição numero 1
if (entrada == "E" or entrada == "e") and senha_digitada == senha_permitida:
    print("Entrar")
#condição numero 2
elif  entrada == "S" or entrada =="s"  :
    print("erro")
#final da condição 
else:
    print("erro")
