class Cliente:
    def __init__(self,cpf,nome,endereco) :
        self.cpf=cpf
        self.nome=nome
        self.endereco=endereco

    def exibir_clientes(self):
        print(f"cliente")