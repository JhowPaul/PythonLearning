from ContaPoupanca import ContaPoupança
from Contas import Conta
from ContaCliente import ContaCliente


class ContaRemunerada(Conta,ContaPoupança):
    def __init__(self,taxaremuneracao, clientes, numero, saldo):
        super().__init__(clientes, numero, saldo)
        super().__init__(self,taxaremuneracao,saldo)
        self.taxaremuneracao=taxaremuneracao

    def remuneraConta(self):
        self.saldo+=self.saldo*(self.taxaremuneracao/30)
        self.saldo-=self.taxaremuneracao

class ContaRemunerada(ContaCliente):
    def __init__(self, numero, IOF, IR, valorinvestido, taxarendimento):
        super().__init__(numero, IOF, IR, valorinvestido, taxarendimento)

    def CalculoRendimento(self):
        self.valorinvestido+=(self.valorinvestido*self.taxarendimento)
        self.valorinvestido-=self.valorinvestido*self.IOF