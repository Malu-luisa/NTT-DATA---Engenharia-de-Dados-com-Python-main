# Função dir() e help()

# A função dir() retorna a lista de métodos e atributos que o objeto pode acessar ou executar.
exemplo = "Maria Luisa"  # Definindo a variável 'exemplo' como uma string
print(dir(exemplo))  # Exibe todos os métodos e atributos disponíveis para o objeto do tipo string (str)
# >>> ['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', ...]

# A função help() fornece informações detalhadas sobre o objeto, como seu uso, argumentos, e descrição de métodos.
help(exemplo.upper)  # Exibe a documentação do método 'upper()' da string, mostrando como ele pode ser usado
# >>> Help on built-in function upper:
# >>> upper() method of builtins.str instance
# >>>    Return a copy of the string converted to uppercase.
