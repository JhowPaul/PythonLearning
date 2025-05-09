from Contas import Conta
from Extrato import Extrato
from Clientes import Cliente
import datetime

class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo,limite):
        super().__init__(clientes, numero, saldo) #é possivel instancia-la usando super() ou o proprio 
        self.limite=limite                                                          #nome da classe
    

    
    def sacar(self,valor):
        if (self.saldo+self.limite)< valor:
            return False
        else:
            self.saldo-=valor
            self.extrato.transacoes.append(["SAQUE",valor, "Data", datetime.datetime.today()])
            return True

    