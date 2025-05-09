from Extrato import Extrato

class Banco:
    def __init__(self,codigo,nome):
        self.codigo=codigo
        self.nome=nome
        
        self.contas=[]

    def adicionaConta(self,contacliente):
        self.contas.append(contacliente)

    def calculaRend(self):
        for c in self.contas:
            c.CalculoRendimento()
    
    def imprimeSaldo(self):
        for c in self.contas:
            c.Extrato()
