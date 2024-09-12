# Operadores numéricos
produto1 = 20  # Definindo a variável 'produto1' com valor 20
produto2 = 10  # Definindo a variável 'produto2' com valor 10

# Soma
print(produto1 + produto2)  # Adição: soma os valores de 'produto1' e 'produto2'
# >>> 30

# Subtração
print(produto1 - produto2)  # Subtração: subtrai 'produto2' de 'produto1'
# >>> 10

# Divisão
print(produto1 / produto2)  # Divisão: divide 'produto1' por 'produto2' (resultado em float)
# >>> 2.0

# Divisão inteira
print(produto1 // produto2)  # Divisão inteira: divide 'produto1' por 'produto2', descartando a parte decimal
# >>> 2

# Multiplicação
print(produto1 * produto2)  # Multiplicação: multiplica 'produto1' por 'produto2'
# >>> 200

# Exponenciação
print(produto1 ** produto2)  # Exponenciação: eleva 'produto1' à potência de 'produto2'
# >>> 10240000000000

# Módulo
print(produto1 % produto2)  # Módulo: resto da divisão de 'produto1' por 'produto2'
# >>> 0

# Precedência de operadores

# Primeiro, o cálculo entre parênteses é feito, depois a multiplicação
x = (10 + 5) * 4  # Soma dentro dos parênteses, depois multiplica por 4
print(x)
# >>> 60

# A precedência é: exponenciação (**) > multiplicação/divisão > soma/subtração
y = 10 / 2 + 25 * 2 - 100 ** 2
# 100 ** 2 = 10000, depois 10 / 2 = 5, 25 * 2 = 50, e finalmente 5 + 50 - 10000
print(y)
# >>> -9945.0
