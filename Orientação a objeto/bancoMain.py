from Banco import Banco
from ContaComum import ContaComum
from ContaRemunerada import ContaRemunerada
from ContaCliente import ContaCliente

banco1 = Banco(999,"teste")
contacliente1 = ContaCliente (1,0.01,0.1,1000,0.05)
contacomum1 = ContaComum(2,0.01,0.1,2000,0.05)
contaremunerada1 = ContaRemunerada(3,0.01,0.1,2000,0.05)

banco1.adicionaConta(contacliente1) 
banco1.adicionaConta(contacomum1)
banco1.adicionaConta(contaremunerada1) 
banco1.calculaRend()
banco1.imprimeSaldo() 