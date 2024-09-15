#Função def 

# Função para dizer olá a uma pessoa
def dizer_ola(nome):
    # Exibe uma saudação personalizada com o nome fornecido
    print(f'Olá, {nome}! Como vai você hoje?')

# Solicita ao usuário o seu nome e chama a função 'dizer_ola' com o nome fornecido
dizer_ola(input('Qual seu nome? '))

# Função para fazer um personagem dizer uma frase
def falar(personagem, frase):
    # Exibe uma fala do personagem com a frase fornecida
    print(f'{personagem} diz: {frase}')

# Exemplos de chamadas da função 'falar' com diferentes personagens e frases
falar('Emilly', 'Vamos para a batalha!')
falar('João', 'Eu estou pronto!')

# Função para salvar as informações de um carro
def salvar_carro(marca, modelo, ano, placa):
    # Exibe uma mensagem de sucesso com os dados do carro inserido
    print(f'Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}')

# Solicita ao usuário as informações do carro
carro = {
    'marca': input('Marca: '),
    'modelo': input('Modelo: '),
    'ano': input('Ano: '),
    'placa': input('Placa: ')
}

# Chama a função 'salvar_carro' passando o dicionário desempacotado
salvar_carro(**carro)

# Usando *args e **kwargs

def exibir_poema(data_formatada, *linhas_poema, **informacoes_autor_ano):
    # Junta todas as linhas do poema em uma única string, separadas por novas linhas
    texto_poema = '\n'.join(linhas_poema)
    # Cria uma lista de strings formatadas para cada autor e ano
    metadados_autor_ano = [f'{autor.title()}: {ano}' for autor, ano in informacoes_autor_ano.items()]
    # Concatena todos os dados em uma única mensagem
    mensagem_completa = f'{data_formatada}\n\n{texto_poema}\n\n{"\n".join(metadados_autor_ano)}'
    # Imprime a mensagem
    print(mensagem_completa)

# Solicita ao usuário as informações
data_formatada = input('Qual data? (por extenso) ')
texto_poema = input('Bote o poema: ')

# Cria um dicionário para armazenar autor e ano
informacoes_autor_ano = {}
nome_autor = input('Autor: ')
ano_publicacao = input('Ano: ')
informacoes_autor_ano[nome_autor] = ano_publicacao

# Chama a função com os dados fornecidos
exibir_poema(data_formatada, texto_poema,**informacoes_autor_ano)

#Parâmetros Especiais(/,*)

def exemplo(a, b, /, c, d):
    print(f'Parâmetro a (só por posição): {a}')
    print(f'Parâmetro b (só por posição): {b}')
    print(f'Parâmetro c (pode ser por nome ou posição): {c}')
    print(f'Parâmetro d (pode ser por nome ou posição): {d}')

# Chamada da função com parâmetros por posição
exemplo(1, 2, c=3, d=4)

# Isso vai gerar um erro
# exemplo(a=1, b=2, c=3, d=4)  # TypeError: got some positional-only arguments

def exemplo(a, b, *, c, d):
    print(f'Parâmetro a: {a}')
    print(f'Parâmetro b: {b}')
    print(f'Parâmetro c (só por nome): {c}')
    print(f'Parâmetro d (só por nome): {d}')

# Chamada da função
exemplo(1, 2, c=3, d=4)

# Escopo Local e Global

#global 

# Variável global que armazena o valor do salário
salario = 2000

# Função que adiciona um bônus ao salário e manipula uma lista
def salario_bonus(bonus, lista):
    # Indica que estamos utilizando a variável global 'salario'
    global salario
    
    # Cria uma cópia da lista passada como argumento para evitar modificá-la diretamente
    lista_aux = lista.copy()
    
    # Adiciona o número 2 à lista auxiliar (a cópia)
    lista_aux.append(2)
    
    # Imprime a lista auxiliar, que é a cópia modificada
    print(f"lista_aux={lista_aux}")
    
    # Adiciona o valor do bônus ao salário global
    salario += bonus
    
    # Retorna o novo valor do salário atualizado
    return salario

# Lista original, que será passada como argumento para a função
lista = [1]

# Chama a função passando o bônus de 500 e a lista, e armazena o valor retornado (novo salário) na variável 'salario_com_bonus'
salario_com_bonus = salario_bonus(500, lista)  # O salário agora será 2000 + 500 = 2500

# Imprime o valor do salário atualizado após o bônus
print(salario_com_bonus)  # Saída esperada: 2500

# Imprime a lista original para mostrar que ela não foi modificada (já que trabalhamos com uma cópia dentro da função)
print(lista)  # Saída esperada: [1]

#Local

def calcular_area_quadrado(lado):
    # Variável 'area' é de escopo local, só existe dentro desta função
    area = lado * lado
    return area

# Chamando a função
resultado = calcular_area_quadrado(5)

print(resultado)  # Imprime 25, que é o resultado do cálculo dentro da função

# Se tentarmos acessar a variável 'area' fora da função, causará um erro
# print(area)  # Isso causaria um erro: NameError: name 'area' is not defined
