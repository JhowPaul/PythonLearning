import datetime

class ContaPoupança:

    def __init__(self,taxaremuneracao):
        self.taxaremuneracao=taxaremuneracao
        self.data_abertura=datetime.datetime.today()

    def remuneraConta(self):
        self.saldo+=self.saldo*self.taxaremuneracao