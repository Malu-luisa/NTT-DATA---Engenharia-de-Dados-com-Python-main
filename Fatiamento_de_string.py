# Definindo a variável 'nome' com o valor atribuído
nome = 'Maria Luisa De Castro Ferreira'

# Acessando o primeiro caractere da string (índice 0)
print(nome[0])  # Saída: 'M'

# Acessando os primeiros 5 caracteres da string (índice 0 até 4)
print(nome[:5])  # Saída: 'Maria'

# Acessando a substring a partir do índice 10 até o final
print(nome[10:])  # Saída: 'ro Ferreira'

# Acessando a substring do índice 10 ao índice 15 (não inclui o índice 16)
print(nome[10:16])  # Saída: 'a De C'

# Acessando os caracteres do índice 10 ao 15 com um passo de 2 (pulando 1 caractere a cada 2)
print(nome[10:16:2])  # Saída: 'a eC'

# Acessando a string completa
print(nome[:])  # Saída: 'Maria Luisa De Castro Ferreira'

# Invertendo a string com o passo -1 (de trás para frente)
print(nome[::-1])  # Saída: 'arierreF ortsaC eD asiuL airaM'

