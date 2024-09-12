# IMPORTANTE: Códigos em Python sempre precisam ser indentados corretamente

# Exemplo correto de indentação
def sacar(valor):  # Define a função 'sacar' que recebe um parâmetro 'valor'
    saldo = 500     # Define a variável 'saldo' dentro da função

    if saldo >= valor:  # Verifica se o saldo é suficiente para o valor desejado
        print('Valor sacado!')  # Executado se a condição do 'if' for verdadeira
        print('Retire seu dinheiro na boca do caixa.')  # Executado se a condição do 'if' for verdadeira
    else:
        print('Não foi possível sacar')  # Executado se a condição do 'if' for falsa

sacar(100)  # Chama a função 'sacar' passando 100 como argumento

# Exemplo incorreto de indentação
# Este código está comentado porque não funciona em Python devido à falta de indentação adequada

# def sacar(self, valor: float) -> None:  # Início do bloco do método
# if self.saldo >= valor:  # Início do bloco do 'if'
# self.saldo -= valor  # Linha de código não indentada corretamente

# # Fim do bloco do 'if'
# # Fim do bloco do método
