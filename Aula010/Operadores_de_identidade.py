#São operadores ultilizados para comparar se os dois objetos 
#testados ocupam a mesma posição na memória. 


saldo = 1000
limite = 500

print(saldo is limite)
print(saldo is not limite)

#.................................................

#exemplo

curso = 'Curso de python'
nome_curso = curso 
saldo, limite = 200,200

curso is nome_curso
#>>>True

curso is not nome_curso
#>>>False

saldo is limite 
#>>>True
