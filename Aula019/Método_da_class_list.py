# [].append
lista = []
lista.append(1)
lista.append('Python')
lista.append([40, 30, 20])
print(lista)  # [1, 'Python', [40, 30, 20]]

# [].clear
lista = [1, 'Python', [40, 30, 20]]
print(lista)  # [1, 'Python', [40, 30, 20]]
lista.clear()
print(lista)  # []

# [].copy
lista = [1, 'Python', [40, 30, 20]]
l2 = lista.copy()
print(lista)  # [1, 'Python', [40, 30, 20]]
print(id(l2), id(lista))  # Verifica se são listas diferentes

# [].count
cores = ['vermelho', 'azul', 'verde', 'azul']
print(cores.count('vermelho'))  # 1
print(cores.count('azul'))  # 2
print(cores.count('verde'))  # 1

# [].extend
linguagens = ['python', 'js', 'c']
print(linguagens)  # ['python', 'js', 'c']
linguagens.extend(['java', 'csharp'])
print(linguagens)  # ['python', 'js', 'c', 'java', 'csharp']

# [].index
linguagens = ['python', 'js', 'c', 'java', 'csharp']
print(linguagens.index('java'))  # 3
print(linguagens.index('python'))  # 0

# [].pop
lista = [1, 2, 3, 4]
ultimo = lista.pop()  # Remove e retorna o último elemento
print(ultimo)  # 4
print(lista)  # [1, 2, 3]

lista = [1, 2, 3, 4]
segundo = lista.pop(1)  # Remove o elemento do índice 1
print(segundo)  # 2
print(lista)  # [1, 3, 4]

# [].remove
linguagens = ['python', 'js', 'c', 'java', 'csharp']
linguagens.remove('c')
print(linguagens)  # ['python', 'js', 'java', 'csharp']

# [].reverse
linguagens = ['python', 'js', 'c', 'java', 'csharp']
linguagens.reverse()
print(linguagens)  # ['csharp', 'java', 'c', 'js', 'python']

# [].sort
linguagens = ['python', 'js', 'c', 'java', 'csharp']
linguagens.sort()  # Ordena a lista em ordem alfabética
print(linguagens)  # ['c', 'csharp', 'java', 'js', 'python']

linguagens.sort(reverse=True)  # Ordena a lista em ordem alfabética inversa
print(linguagens)  # ['python', 'js', 'java', 'csharp', 'c']

linguagens.sort(key=lambda x: len(x))  # Ordena pela quantidade de caracteres
print(linguagens)  # ['c', 'js', 'java', 'csharp', 'python']

linguagens.sort(key=lambda x: len(x), reverse=True)  # Ordena do maior para o menor
print(linguagens)  # ['python', 'csharp', 'java', 'js', 'c']

# len
linguagens = ['python', 'js', 'c', 'java', 'csharp']
print(len(linguagens))  # 5

# sorted
linguagens = ['python', 'js', 'c', 'java', 'csharp']
nova_lista = sorted(linguagens, key=lambda x: len(x))  # Ordena por comprimento
print(nova_lista)  # ['c', 'js', 'java', 'csharp', 'python']

nova_lista_decrescente = sorted(linguagens, key=lambda x: len(x), reverse=True)  # Ordem inversa
print(nova_lista_decrescente)  # ['python', 'csharp', 'java', 'js', 'c']
