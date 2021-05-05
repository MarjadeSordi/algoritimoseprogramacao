class Veiculos:
  def __init__(self, marca, qtRodas, modelo, velocidade = 0, velocidadeAtual=0):
    self.marca = marca
    self.qtRodas = qtRodas
    self.modelo = modelo
    self.velocidade = velocidade 
    self.velocidadeAtual = velocidadeAtual

  def getvelocidade(self): 
    return self.velocidade

  def getVelocidadeAtual(self):
    return self.velocidadeAtual

  def acelerar(self):
    return  self.velocidade + self.velocidadeAtual

  def frear(self):
    return self.velocidadeAtual - self.velocidade 


  def imprimirinformacoes(self):
    print ("Marca: " + self.marca +
    "Quantidade de Rodas: " + str(self.qtRodas) + 
    "Modelo: " + self.modelo +
    "Velocidade: " + str(self.velocidade))


a = Veiculos('uno', 5, 'mile', 20, 120)
print(a.acelerar())
print(a.frear())

class Automovel(Veiculos):
  def __init__(self, potenciadoMotor, marca, qtRodas, modelo, velocidade = 0):
    Veiculos.__init__(self, marca, qtRodas, modelo, velocidade = 0)
    self.potenciadoMotor = potenciadoMotor

  def imprimirinformacoes(self):
    print ("Marca: " + self.marca +
    "Quantidade de Rodas: " + str(self.qtRodas) + 
    "Modelo: " + self.modelo +
    "Velocidade: " + str(self.velocidade) +
    "Potencia do Motor" + str(self.potenciadoMotor))


a= Automovel(200, 'fiat', 4, 'ka', 100)
a.imprimirinformacoes()


class Moto(Veiculos):
  def __init__(self, partidaeletrica, marca, qtRodas, modelo, velocidade = 0):
    Veiculos.__init__(self, marca, qtRodas, modelo, velocidade = 0)
    self.partidaeletrica = True; 

  def getPartidaEletrica(self): 
    if(self.partidaeletrica == True):
      return ("Partida eletrica")
    else:
      return ("Não tem partida elétrica ")


  def imprimirinformacoes(self):
    print ("Marca: " + self.marca +
    "Quantidade de Rodas: " + str(self.qtRodas) + 
    "Modelo: " + self.modelo +
    "Velocidade: " + str(self.velocidade))

a = Moto('honda', 2, 'model', 100)
print(a.getPartidaEletrica())

class  Bicicleta(Veiculos):
  def __init__(self, bagageiro, numerodeMarchas, marca, qtRodas, modelo, velocidade = 0):
    Veiculos.__init__(self, marca, qtRodas, modelo, velocidade = 0)
    self.bagageiro = False; 
    self.numerodeMarchas = numerodeMarchas

  def getBagageiro(self): 
    if(self.bagageiro == True):
      return ("Possui Bagageiro")
    else:
      return ("Não possui Bagageiro ")

  def imprimirinformacoes(self):
    print ("Marca: " + self.marca +
    "Quantidade de Rodas: " + str(self.qtRodas) + 
    "Modelo: " + self.modelo +
    "Velocidade: " + str(self.velocidade) +
    "Numero de Marchas"  + str(self.numerodeMarchas))


a = Bicicleta('caloi', 2, 'cesta', 20, 5)
print(a.getBagageiro())

class Carro(Veiculos):
  def __init__(self, quantidadedePortas, marca, qtRodas, modelo, velocidade = 0):
    Veiculos.__init__(self, marca, qtRodas, modelo, velocidade = 0)
    self.quantidadedePortas = quantidadedePortas

  def imprimirinformacoes(self):
    print ("Marca: " + self.marca +
    "Quantidade de Rodas: " + str(self.qtRodas) + 
    "Modelo: " + self.modelo +
    "Velocidade: " + str(self.velocidade) +
    "Quantidade de Portas" + str(self.quantidadedePortas))


a= Carro(2, 'ferrari', 4,'red', 1000)
a.imprimirinformacoes()