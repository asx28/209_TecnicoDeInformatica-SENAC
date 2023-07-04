#exemplos:
nome = '''Amanda'''
idade = 28
altura = 1.55
maior_de_idade = False

#Tipos primitivos
print(nome, type(nome), idade, type(idade), altura, type(altura), maiorDeIdade, type(maiorDeIdade))

#Entrada
salarioBase = 2000
gratificacao = 50

#processamento
salarioBruto = salarioBase+gratificacao

#saida
print("Seu salário bruto é R$", salarioBruto)

class Pessoa():
  def __init__(self, name, age):
    #atributos
    self.nome = name
    self.idade = age

  def apresentacao(self):
    print("Seja bem-vindo!")

class PessoaFisica():
  #construtor
  def __init__(self, name, age, cpf): #variáveis locais
    self.nome = name
    self.idade = age
    self.CPF = cpf

  def apresentacao(self):
    print("Seja bem-vindo!")

  def impostoDeRenda(self, *salarios, taxa=0.015):
    print("Tupla de salários: ", salarios)
    irTotal = 0
    for s in salarios:
      irIndividual = s*taxa
      irTotal = irTotal + irIndividual
    print("O valor do seu imposto de renda é R$", irTotal)
    return irTotal

class PessoaJuridica():
  def __init__(self, nome, idade, cnpj):
    self.nome = nome
    self.idade = idade
    self.CNPJ = cnpj

  def apresentacao(self):
    print("Seja bem-vindo!")

  def impostoDeRenda(self, salario, taxa=0.10):
    IR = salario*taxa
    return IR
