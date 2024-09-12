# Exemplo de Estrutura sem repetição.
# Receba um número do teclado e exiba os 2 números seguintes.
numero = int(input('Informe um número inteiro: '))  # Solicita um número inteiro ao usuário e converte para int
print(numero)  # Exibe o número fornecido
print(numero + 1)  # Exibe o próximo número
print(numero + 2)  # Exibe o número seguinte ao anterior

# Exemplo de Estrutura com repetição
a = int(input('Informe um número inteiro: '))  # Solicita um número inteiro ao usuário e converte para int
print(a)  # Exibe o número fornecido

# Repete 2 vezes
for _ in range(2):  # Loop que será executado 2 vezes
    a += 1  # Incrementa o valor de 'a' em 1
    print(a)  # Exibe o valor de 'a'

# Estrutura for / if
texto = input('Informe um texto: ')  # Solicita um texto ao usuário
VOGAIS = 'AEIOU'  # Define as vogais

for letras in texto:  # Itera sobre cada caractere no texto
    if letras.upper() in VOGAIS:  # Verifica se o caractere é uma vogal
        print(letras, end=" ")  # Exibe a vogal, sem quebrar linha
print()  # Adiciona uma quebra de linha após a lista de vogais

# Estrutura for / else
texto = input('Informe um texto: ')  # Solicita um texto ao usuário
VOGAIS = 'AEIOU'  # Define as vogais

for letras in texto:  # Itera sobre cada caractere no texto
    if letras.upper() in VOGAIS:  # Verifica se o caractere é uma vogal
        print(letras, end=" ")  # Exibe a vogal, sem quebrar linha
else:  # Executa quando o loop termina normalmente
    print()  # Adiciona uma quebra de linha
    print('Executa no final do laço')  # Mensagem exibida após o término do loop

# Função range
# Exibindo a tabuada de 5
for tabuada in range(0, 51, 5):  # Itera de 0 até 50 (inclusive), com um passo de 5
    print(tabuada, end="  ")  # Exibe o valor atual da tabuada, separando por dois espaços

# Estrutura WHILE
opcao = -1  # Inicializa a variável 'opcao' com um valor diferente de 0

while opcao != 0:  # Executa enquanto 'opcao' for diferente de 0
    opcao = int(input('[1] sacar \n[2] Extrato \n[0] sair \n'))  # Solicita a opção ao usuário e converte para int
    if opcao == 1:
        print('Sacando')  # Exibe mensagem para saque
    elif opcao == 2:
        print('Exibindo extrato')  # Exibe mensagem para extrato
