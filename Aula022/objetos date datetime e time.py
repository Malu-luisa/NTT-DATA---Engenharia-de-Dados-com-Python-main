from datetime import date, datetime, timedelta  # Importando as classes necessárias para manipulação de datas e tempos
import pytz  # Importando a biblioteca pytz para manipulação de fusos horários

# Definindo uma data específica
data = date(2024, 10, 11)
print(f'Data específica: {data}')  # Imprimindo a data definida

# Imprimindo a data atual
print(f'Data atual: {date.today()}')

# Definindo uma data e hora específicas
data_hora = datetime(2023, 7, 19)
print(f'Data e hora definidas: {data_hora}')  # Imprimindo a data e hora definidas

# Imprimindo a data e hora atual
print(f'Data e hora atual: {datetime.now()}')

# Adicionando uma semana à data definida
data_futura = data + timedelta(weeks=1)  # Usando timedelta para adicionar uma semana
print(f'Data após adicionar uma semana: {data_futura}')  # Imprimindo a nova data

# Definindo tipos de carro por porte
tipo_carroP = 'P'  # Tipo pequeno
tipo_carroM = 'M'  # Tipo médio
tipo_carroG = 'G'  # Tipo grande

# Definindo os tempos de lavagem para cada porte de carro
tempo_pequeno = 30  # Tempo para carro pequeno em minutos
tempo_medio = 45    # Tempo para carro médio em minutos
tempo_grande = 60   # Tempo para carro grande em minutos

# Capturando a data e hora atuais
data_atual = datetime.now()

# Solicitando ao usuário o porte do veículo
tempo = input('Qual o porte do seu veículo? ').upper()  # Convertendo a entrada para maiúsculas

# Verificando o porte do veículo e calculando o tempo estimado de lavagem
if tempo == tipo_carroP:
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)  # Calculando o tempo de lavagem
    print(f'O carro chegou: {data_atual} e tempo de lavagem: {tempo_pequeno} minutos')
elif tempo == tipo_carroM:
    data_estimada = data_atual + timedelta(minutes=tempo_medio)  # Calculando o tempo de lavagem
    print(f'O carro chegou: {data_atual} e tempo de lavagem: {tempo_medio} minutos')
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)  # Calculando o tempo de lavagem
    print(f'O carro chegou: {data_atual} e tempo de lavagem: {tempo_grande} minutos')

# Calculando a data de um dia anterior à data atual
data_anterior = date.today() - timedelta(days=1)  # Subtraindo 1 dia da data atual
print(f'Data de um dia atrás: {data_anterior}')  # Imprimindo a data de um dia atrás

# Calculando o horário subtraindo 1 hora de uma data e hora específica
resultado = datetime(2024, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(f'Horário após subtrair 1 hora: {resultado.time()}')  # Imprimindo somente o horário após subtrair 1 hora

# Imprimindo a data atual
print(f'Data atual novamente: {datetime.now().date()}')

# Convertendo uma string de data em objeto datetime
date_string = '20/07/2023 15:30'
d = datetime.strptime(date_string, "%d/%m/%Y %H:%M")  # Corrigido para '%H:%M' já que a string não inclui segundos
print(f'Data convertida: {d}')  # Saída: 2023-07-20 15:30:00

# Formatando a data atual como string
bonitinho = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print(f'Data atual formatada: {bonitinho}')  # Imprimindo a data atual formatada

# Obtendo a data e hora atuais com fuso horário
data = datetime.now(pytz.timezone('America/Sao_Paulo'))  # Usando a classe datetime e o fuso horário correto
print(f'Data e hora com fuso horário: {data}')  # Imprimindo a data e hora com fuso horário

# Criando datetime com timezone
data = datetime.now(datetime.timezone(datetime.timedelta(hours=-3)))  # Obtém a data e hora atuais no fuso horário UTC-3 (como no Brasil).
print(data)  # Mostra a data e hora atuais no fuso horário definido.

# Convertendo para outro timezone (UTC)
data_utc = data.astimezone(datetime.timezone.utc)  # Converte a data e hora obtidas para o fuso horário UTC (tempo universal).
print(data_utc)  # Mostra a data e hora convertidas para o fuso horário UTC.
