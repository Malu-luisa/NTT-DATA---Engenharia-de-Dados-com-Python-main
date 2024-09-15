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

