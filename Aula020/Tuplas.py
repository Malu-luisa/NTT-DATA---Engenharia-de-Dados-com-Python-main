# frutas: Uma tupla contendo três strings, cada uma representando uma fruta.
# Como as tuplas são imutáveis, uma vez definidas, você não pode adicionar, remover ou alterar elementos diretamente.
frutas = ('laranja', 'pera', 'uva',)

# letras: Esta tupla foi criada a partir de uma string 'python'.
# Quando você passa uma string para o construtor de tupla tuple(), Python converte cada caractere da string em um elemento da tupla.
letras = tuple('python')

# numeros: Similar à tupla de letras, esta é criada a partir de uma lista de números [1, 2, 3, 4].
# A função tuple() converte a lista em uma tupla, tornando-a imutável.
numeros = tuple([1, 2, 3, 4])

# pais: Uma tupla com apenas um elemento.
# É importante notar que para criar uma tupla com um único elemento, você deve incluir uma vírgula após o elemento,
# caso contrário, Python não reconhece a expressão como uma tupla.
pais = ('Brasil',)

# frutas: Aqui, redefinimos a tupla frutas para incluir a fruta 'pera' duas vezes.
# Em seguida, usamos o método count() para contar quantas vezes 'pera' aparece na tupla.
frutas = ('laranja', 'pera', 'uva', 'pera')
contagem = frutas.count('pera')
print(contagem)  # Saída: 2

# frutas: Redefinimos novamente a tupla frutas e usamos o método index() para encontrar o índice da primeira ocorrência de 'uva'.
frutas = ('laranja', 'pera', 'uva')
indice = frutas.index('uva')
print(indice)  # Saída: 2

# frutas: Usamos a função len() para obter o número total de elementos na tupla.
frutas = ('laranja', 'pera', 'uva')
tamanho = len(frutas)
print(tamanho)  # Saída: 3
