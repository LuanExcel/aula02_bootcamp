CONSTANTE_BONUS = 1000

# Solicite ao usuario que digite o seu nome
nome_usuario = input("Digite o seu nome:")

#parasair da execução caso não atenda a condição
# Se não digitou letras
if nome_usuario.isdigit():
    print("Voce digitou o nome errado")
    exit()
# Se não digitou nada    
elif len(nome_usuario) == 0:
    print("Você não digitou nada")
    exit() 
# Se só digitou espaço    
elif nome_usuario.isspace():
    print("Você só digtou espaço")
    exit()       
    