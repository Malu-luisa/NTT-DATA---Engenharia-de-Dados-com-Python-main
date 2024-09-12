nome = 'Maria Luisa'  # Definindo a variável 'nome'
idade = 28  # Definindo a variável 'idade'
profissao = 'Programador'  # Definindo a variável 'profissao'
linguagem = 'Python'  # Definindo a variável 'linguagem'
saldo = 45.435  # Definindo a variável 'saldo'

dados = {'nome': 'Maria Luisa', 'idade': 28}  # Criando um dicionário 'dados' com as chaves 'nome' e 'idade'

# Formatação de string usando o método de substituição por percentual (%)
print('Nome: %s Idade %d' % (nome, idade))  # %s substitui strings, %d substitui inteiros

# Formatação usando o método 'format()' - básica
print('Nome: {} Idade: {}'.format(nome, idade))  # {} são placeholders que são substituídos pelos valores em 'format'

# Formatação usando índices para modificar a ordem dos valores passados
print('Nome: {1} Idade: {0}'.format(idade, nome))  # {1} refere-se ao segundo argumento, {0} ao primeiro

# Mais placeholders e repetição do mesmo valor várias vezes
print('Nome: {1} Idade: {0}  Nome: {1} {1} {1}'.format(idade, nome))  # Nome será repetido várias vezes usando {1}

# Utilizando parâmetros nomeados no 'format()'
print('Nome: {nome}  Idade: {idade}'.format(nome=nome, idade=idade))  # Atribuição de valores diretamente no 'format()'

# Usando o mesmo valor várias vezes em uma única string
print('Nome: {nome} Idade: {age} {nome} {nome} {age}'.format(age=idade, nome=nome))  # {nome} e {age} usados múltiplas vezes

# Utilizando o dicionário 'dados' para preencher os placeholders
print('Nome: {nome} Idade: {idade}'.format(**dados))  # '**dados' expande o dicionário, passando os valores para os placeholders

# Formatação com f-strings (disponível a partir do Python 3.6)
print(f'Nome: {nome} Idade: {idade}')  # f-strings permitem inserir variáveis diretamente dentro das chaves

# f-strings com formatação de número (com duas casas decimais)
print(f'Nome: {nome} Idade: {idade} saldo: {saldo:0.2f}')  # Formata o saldo com 2 casas decimais

# Formatação do saldo com espaçamento (campo de 10 caracteres, incluindo os dígitos e o ponto decimal)
print(f'Nome: {nome} Idade: {idade} saldo: {saldo:10.2f}')  # Reserva 10 espaços para exibir o saldo, alinhando à direita