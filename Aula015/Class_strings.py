# Conhecendo métodos úteis da classe String
Curso = 'pYtHon'  # Definindo a variável 'Curso' com o valor 'pYtHon'

# Maiúscula
print(Curso.upper())  # O método upper() transforma todos os caracteres da string em maiúsculas
# >>> PYTHON

# Minúscula
print(Curso.lower())  # O método lower() transforma todos os caracteres da string em minúsculas
# >>> python

# Título
print(Curso.title())  # O método title() coloca a primeira letra de cada palavra em maiúscula
# >>> Python

# Eliminando espaços em branco
curso = '    Python'  # Definindo a variável 'curso' com espaços em branco antes da palavra 'Python'

print(curso.strip())  # O método strip() remove espaços em branco no início e no final da string
# >>> 'Python'

print(curso.lstrip())  # O método lstrip() remove apenas os espaços à esquerda (início) da string
# >>> 'Python '

print(curso.rstrip())  # O método rstrip() remove apenas os espaços à direita (final) da string
# >>> ' Python'

# Junções e centralizações
curso = 'Python'  # Redefinindo a variável 'curso' com o valor 'Python'

print(curso.center(10, '#'))  # O método center() centraliza a string, preenchendo o espaço restante com '#'
# >>> '##Python##'

print('.'.join(curso))  # O método join() insere um caractere ('.') entre cada letra da string
# >>> 'P.y.t.h.o.n'

# EXEMPLO:

nome = 'MaRia LuISa'  # Definindo a variável 'nome' com o valor 'MaRia LuISa'

print(nome.upper())  # O método upper() transforma todos os caracteres da string em maiúsculas
# >>> MARIA LUISA

print(nome.lower())  # O método lower() transforma todos os caracteres da string em minúsculas
# >>> maria luisa

print(nome.title())  # O método title() coloca a primeira letra de cada palavra em maiúscula
# >>> Maria Luisa

texto = '    Amo Fernando!     '  # Definindo a variável 'texto' com espaços em branco ao redor da string

print(texto.strip())  # O método strip() remove espaços em branco no início e no final da string
# >>> Amo Fernando

print(texto.lstrip())  # O método lstrip() remove os espaços à esquerda da string
# >>> Amo Fernando!   

print(texto.rstrip())  # O método rstrip() remove os espaços à direita da string
# >>>    Amo Fernando

menu = 'Python'  # Definindo a variável 'menu' com o valor 'Python'

print(menu.center(14))  # O método center() centraliza a string em um espaço de 14 caracteres
# >>>    Python    

print(menu.center(14,'.'))  # O método center() centraliza a string e preenche o espaço restante com '.'
# >>> ....Python....

print('###',menu,'###')  # Usando vírgulas para concatenar a string 'menu' com outros caracteres
# >>> ### Python ###

print('$'.join(menu))  # O método join() insere um caractere ('$') entre cada letra da string
# >>> P$y$t$h$o$n
