class Retangulo:
  def __init__(self, largura, altura):
    self.largura = largura
    self.altura = altura
    self.area = int(area)


    def getAltura(self):
      return self.altura 

    def getLargura(self):
      return self.largura

    def getArea(self):
      return self.area


##funções
def RegistraAltura():
  altura = int(input('Digite a altura do retangulo: '))
  largura = int(input('Digite a altura do retangulo; '))
  area = altura * largura
  return print (('A area do retangulo é: ') + str(area))


  
        

def menu():
    while True:
        print('''Digite: 
        1- para calcular a área de um retangulo;
        0 - para sair''')
        consulta= input ('')
        if consulta == '0':break 
        elif consulta == '1': RegistraAltura()
      
   


menu()