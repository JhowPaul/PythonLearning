from abc import ABC ,abstractmethod

class ContaCliente(ABC):

    def __init__(self, numero, IOF,IR,valorinvestido,taxarendimento):
        self.numero = numero
        self.IOF = IOF
        self.IR = IR
        self.valorinvestido = valorinvestido
        self.taxarendimento = taxarendimento

    @abstractmethod
    def CalculoRendimento(self):
        pass
        self.valorinvestido += (self.valorinvestido * self.taxarendimento)
        self.valorinvestido = self.valorinvestido - (self.taxarendimento * self.IOF* self.IR)

    def Extrato(self): #self estava escrito errado
        print (f"O saldo atual da conta {self.numero} é {self.valorinvestido:10.2f}")