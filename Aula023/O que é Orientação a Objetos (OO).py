class Cachorro:
    # Método construtor que inicializa os atributos de cada objeto da classe
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome          # Nome do cachorro (ex: 'Chappie', 'Aladim')
        self.cor = cor            # Cor do cachorro (ex: 'amarelo', 'branco e preto')
        self.acordado = acordado  # Indica se o cachorro está acordado (padrão é True)
        
    # Método que simula o latido do cachorro
    def latir(self):
        print('Auau')             # Exibe 'Auau' no terminal quando o cachorro late
        
    # Método que simula o cachorro dormindo
    def dormir(self):
        self.acordado = False     # Define o atributo 'acordado' como False
        print('Zzzzzz...')        # Exibe 'Zzzzzz...', indicando que o cachorro está dormindo

# Criando os objetos (instâncias da classe Cachorro)
cao_1 = Cachorro('Chappie', 'amarelo', False)  # Cachorro 1: nome 'Chappie', cor 'amarelo', acordado False (dormindo)
cao_2 = Cachorro('Aladim', 'branco e preto')   # Cachorro 2: nome 'Aladim', cor 'branco e preto', acordado True (padrão)

# Chamando os métodos e verificando os atributos
cao_1.latir()            # O método latir é chamado para 'Chappie', imprimindo 'Auau'
print(cao_2.acordado)    # Verifica se 'Aladim' está acordado, imprime True (valor padrão do atributo)
cao_2.dormir()           # O método dormir é chamado para 'Aladim', imprimindo 'Zzzzzz...' e mudando o estado de 'acordado' para False
print(cao_2.acordado)    # Verifica se 'Aladim' está acordado, imprime False (após chamar o método dormir)


class Bicicleta:
    # Método construtor que inicializa os atributos de cada objeto da classe
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor          # A cor da bicicleta (ex: 'Azul', 'Rosa')
        self.modelo = modelo    # O modelo da bicicleta (ex: 'Radical', 'Criança')

        self.ano = ano          # O ano de fabricação da bicicleta (ex: 2009, 2023)
        self.valor = valor      # O valor da bicicleta (ex: 1200, 400000)

    # Método para simular o som da buzina da bicicleta
    def buzinar(self):
        print('BIBIIIIIIIIII')   # Exibe no terminal o som "BIBIIIIIIIIII"

    # Método que simula a bicicleta parando
    def parar(self):
        print('Stop')            # Exibe a palavra 'Stop' para indicar a parada

    # Método que simula a bicicleta correndo
    def correr(self):
        print("zzzunnnnnnnn")    # Exibe o som "zzzunnnnnnnn", simulando a bicicleta em movimento

    # Método especial __str__, que retorna uma representação textual da bicicleta
    # Essa função é chamada automaticamente quando usamos print em um objeto da classe Bicicleta
    def __str__(self):
        # Retorna o nome da classe (Bicicleta), seguido de uma string formatada que exibe todos os atributos da bicicleta
        # O dicionário self.__dict__ contém os atributos do objeto e seus valores.
        return f"{self.__class__.__name__}: {{ " + ', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()]) + " }}"

# Simulação da venda de bicicletas
# Criando uma instância (objeto) da classe Bicicleta com os atributos definidos
bicicleta1 = Bicicleta('Azul', 'Radical', 2009, 1200)  # Uma bicicleta azul, modelo 'Radical', ano 2009, valor 1200
bicicleta2 = Bicicleta('Rosa', 'Criança', 2023, 400000)  # Outra bicicleta rosa, modelo 'Criança', ano 2023, valor 400000

# Chamando o método buzinar na bicicleta1
bicicleta1.buzinar()  # Exibe "BIBIIIIIIIIII"

# Exibindo as informações da bicicleta1
# Isso automaticamente chama o método __str__, que retorna a string formatada com os atributos
print(bicicleta1)  # Exibe: Bicicleta: { cor=Azul, modelo=Radical, ano=2009, valor=1200 }

# Chamando o método parar na bicicleta2
bicicleta2.parar()  # Exibe "Stop"

# Exibindo as informações da bicicleta2
print(bicicleta2)  # Exibe: Bicicleta: { cor=Rosa, modelo=Criança, ano=2023, valor=400000 }
