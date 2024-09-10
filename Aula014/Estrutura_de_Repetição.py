# Exemplo de Estrutura sem repetição.
# Receba um número do telcado e exiba os 2 números seguintes. 
#........................................................................
# Exemplo de Estrutura com repetição
a = int(input('Informe um número inteiro: '))
print(a)

a += 1 
print(a)

a += 1 
print(a)
# ..........
# a = int(input('Informe um número: '))
# print(a)

# repita 2 vezes: 
#   a+= 1 
#   print(a)
# ..................................................................................

# Estrutura for / if 
texto = input('Informe um texto: ')
VOGAIS = 'AEIOU'

for letras in texto: 
    if letras.upper() in VOGAIS:
        print(letras, end=" ")
print()


#Estrutura for/else
texto = input('Informe um texto: ')  
VOGAIS = 'AEIOU'  

for letras in texto: 
    if letras.upper() in VOGAIS:  
        print(letras, end=" ") 
else: 
    print()  
    print('Executa no final do laço')

#Função range 

#exibindo a tabuada de 5 

for tabuada in range(0,51,5):
    print(tabuada, end="  ")

#Estrutura WHILE

opcao = -1

while opcao != 0: 
    opcao = int(input('[1] sacar \n[2] Extrato \n[0] sair \n'))
    if opcao == 1:
         print('Sacando')
    elif opcao == 2:
         print('Exibindo extrato')
         