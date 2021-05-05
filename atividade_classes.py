



class Aluno:
  nome = []
  matricula = []

  def __init__(self, nome, matricula):
    self.nome = nome
    self.matricula= matricula

  def imprimir(self):
    print ('Nome: ' + self.nome + ' ' + 'Matrícula: ' + self.matricula)


aluno = Aluno ('Marja', '2')
aluno.imprimir()


class AlunoEnsinoMedio(Aluno):
  ano = []

  def __init__(self, ano, nome, matricula):
    Aluno.__init__(self, nome, matricula)
    self.ano = ano

  def imprimir(self):
    print ('Nome: ' + self.nome + ' ' + 'Matrícula: ' + self.matricula + ' Ano: ' + self.ano)


alunomedio = AlunoEnsinoMedio('2020', 'Marja','2')
alunomedio.imprimir()


class AlunoGraduacao(Aluno):
  semestre = []

  def __init__(self, semestre, nome, matricula):
    Aluno.__init__(self, nome, matricula)
    self.semestre = semestre

  def imprimir(self):
    print ('Nome: ' + self.nome + ' ' + 'Matrícula: ' + self.matricula + ' Semestre: ' + self.semestre)


alunograduacao = AlunoGraduacao('4', 'Marja', '2021')
alunograduacao.imprimir()

