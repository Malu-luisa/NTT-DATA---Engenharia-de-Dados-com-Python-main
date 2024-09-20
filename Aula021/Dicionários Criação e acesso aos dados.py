# Definindo um dicionário chamado "contatos" com emails como chave e informações dos contatos como valor
contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '1234-1234'},
    'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '1345-1098'},
    'chappie@gmail.com': {'nome': 'Chappie', 'telefone': '1564-7654'},
    'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '1987-3454', 'extra': {'a': 1}}
}

# Acessando o telefone de Giovanna e imprimindo o resultado
telefone = contatos['giovanna@gmail.com']['telefone']
print(telefone)  # Saída: 1345-1098

# Acessando todas as informações de Melaine e imprimindo o resultado
extra = contatos['melaine@gmail.com']
print(extra)  # Saída: {'nome': 'Melaine', 'telefone': '1987-3454', 'extra': {'a': 1}}

# Definindo um novo dicionário chamado "dados" com informações pessoais
dados = {'nome': 'Jean', 'idade': 28, 'telefone': '999999999999'}

# Acessando e atualizando os valores no dicionário "dados"
dados['nome']  # Saída: 'Jean'
dados['idade']  # Saída: 28
dados['telefone']  # Saída: '999999999999'

# Modificando os valores de "dados"
dados['nome'] = 'Maria'
dados['idade'] = '18'
dados['telefone'] = '40028922'

# Exibindo o dicionário atualizado
print(dados)  # Saída: {'nome': 'Maria', 'idade': 18, 'telefone': '40028922'}

# Iterando sobre as chaves do dicionário "contatos" e imprimindo cada uma com seus valores correspondentes
for chave in contatos:
    print(chave, contatos[chave])

# Usando .items() para obter as chaves e valores e imprimindo
for chave, valor in contatos.items():
    print(chave, valor)

# Criando um novo dicionário "contatos" sem o campo "extra"
contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '1234-1234'},
    'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '1345-1098'},
    'chappie@gmail.com': {'nome': 'Chappie', 'telefone': '1564-7654'},
    'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '1987-3454'}
}

# Limpando o dicionário "contatos"
contatos.clear()
print(contatos)  # Saída: {}

# Redefinindo o dicionário "contatos" com um único contato
contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '1234-1234'}
}

# Criando uma cópia do dicionário "contatos" e tentando modificar o valor copiado (com erro de sintaxe corrigido)
copia = contatos.copy()
copia['guilherme@gmail.com'] = {'nome': 'gui'}  # Corrigido para "copia"

# Imprimindo os valores da cópia e do original
print(contatos['guilherme@gmail.com'])  # Saída: {'nome': 'Guilherme', 'telefone': '1234-1234'}
print(copia['guilherme@gmail.com'])  # Saída: {'nome': 'gui'}

# Criando um dicionário a partir de uma lista de animais, atribuindo o mesmo valor a todas as chaves
animais = ['gato', 'cachorro', 'pássaro']
painel = dict.fromkeys(animais, 'biscoito')
print(painel)  # Saída: {'gato': 'biscoito', 'cachorro': 'biscoito', 'pássaro': 'biscoito'}

# Criando um dicionário com valores padrão None (vazio)
painel_vazio = dict.fromkeys(animais)
print(painel_vazio)  # Saída: {'gato': None, 'cachorro': None, 'pássaro': None}

# Verificando se a chave 'chaves' existe no dicionário "contatos" (deve dar erro)
contatos['chaves']  # Isso dará KeyError porque 'chaves' não existe

# Usando o método .get() para evitar o erro de chave inexistente
print(contatos.get('chaves'))  # Saída: None
print(contatos.get('chave', {}))  # Saída: {}
print(contatos.get('guilherme@gmail.com', {}))  # Saída: {'nome': 'Guilherme', 'telefone': '1234-1234'}

# Iterando sobre o dicionário "contatos" e imprimindo as chaves e valores formatados
contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'telefone': '1234-1234'},
    'maria@gmail.com': {'nome': 'Maria', 'telefone': '5678-5678'}
}

for chave, valor in contatos.items():
    print(f'Chave: {chave}, Valor: {valor}')
