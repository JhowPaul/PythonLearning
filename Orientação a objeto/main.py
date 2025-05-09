#from Conta import Conta
from Contas import Conta
from Clientes import Cliente
from Extrato import Extrato
from ContaEspecial import ContaEspecial
from ContaPoupanca import ContaPoupança
from ContaRemunerada import ContaRemunerada

cliente3=Cliente(1234,"Ringo","Abbey Road")
cliente4=Cliente(567,"Daft Punk","Random Acess Memory")
cliente5=Cliente("789","Spididif","Arandu")
conta1=Conta([cliente3,cliente4], 1,200)
conta2=ContaEspecial([cliente5],3,1000,2000)
contapoupanca=ContaPoupança(0.1)
conteremunerada=ContaRemunerada(0.1,cliente5,5,1000)

conteremunerada.remuneraConta()
conteremunerada.gerarsaldo()
conta2.depositar(100)
conta2.sacar(200)
conta2.extrato.extrato(conta2.numero)
conta1.depositar(1500)
conta1.sacar(200)
conta1.extrato.extrato(conta1.numero)





#print("Conta 1")
#c1=Conta(1,1,"joao",1000)
#c1.depositar(300)
#c1.sacar(100)
#c1.gerar_extrato()

#print("\nConta 2")
#c2=Conta(2,2,"Maria",0000)
#c2.depositar(50)
#c2.sacar(10)
#c2.gerar_extrato()

#print("\n")
#c1.transf_valor(c2,200)
#print(c1.saldo)
#print(c2.saldo)