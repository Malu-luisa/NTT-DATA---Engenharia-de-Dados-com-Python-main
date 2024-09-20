# Criando um conjunto (set) a partir de uma lista com valores repetidos
# Os sets não permitem duplicatas, então o resultado será {1, 2, 3, 4}
set([1, 2, 3, 1, 3, 4])  # {1, 2, 3, 4}

# Criando um conjunto a partir de uma string
# Os sets quebram a string em caracteres únicos, sem repetição
set('abacaxi')  # {'b', 'a', 'c', 'x', 'i'}

# Criando um conjunto a partir de uma tupla com valores repetidos
# Valores duplicados são removidos, resultado será {'gol', 'celta', 'palio'}
set(('palio', 'gol', 'celta', 'palio'))  # {'gol', 'celta', 'palio'}

# Criando um conjunto de linguagens de programação
# Sets ignoram valores duplicados, então 'java' será armazenado uma única vez
linguagens = {'pyhton', 'java', 'java'}
print(linguagens)  # {'pyhton', 'java'}

# Acessando elementos de um set
# Aqui criamos um set de números com alguns repetidos
numeros = {1, 2, 3, 2}

# Convertendo o set em uma lista para acessar pelo índice
numeros = list(numeros)
print(numeros[0])  # Exibe o primeiro número (a ordem não é garantida)

# Iterando sobre um conjunto de carros
carros = {'gol', 'celta', 'palio'}

# Imprimindo cada carro do set
for carro in carros:
    print(carro)

# Enumerando elementos de um set
# O enumerate permite associar um índice a cada item do set
for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')

# Operações com sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# União de dois sets (combina os elementos, sem repetição)
print(set1.union(set2))  # Saída: {1, 2, 3, 4, 5}

# Interseção (elementos comuns a ambos os sets)
print(set1.intersection(set2))  # Saída: {3}

# Diferença entre dois sets
# Elementos presentes em set1, mas não em set2
print(set1.difference(set2))  # Saída: {1, 2}
# Elementos presentes em set2, mas não em set1
print(set2.difference(set1))  # Saída: {4, 5}

# Diferença simétrica (elementos que estão em um dos sets, mas não em ambos)
print(set1.symmetric_difference(set2))  # Saída: {1, 2, 4, 5}

# Subset (verifica se um conjunto está contido em outro)
set1 = {1, 2, 3}
set2 = {4, 1, 2, 5, 6, 3}
print(set1.issubset(set2))  # True, set1 está contido em set2
print(set2.issubset(set1))  # False, set2 não está contido em set1

# Superset (verifica se um conjunto contém outro)
print(set1.issuperset(set2))  # False, set1 não contém set2
print(set2.issuperset(set1))  # True, set2 contém set1

# Verificando relações entre sets adicionais
set3 = {1, 0}
print(set1.issuperset(set2))  # False, set1 não contém set2
print(set1.issuperset(set3))  # False, set1 não contém set3
