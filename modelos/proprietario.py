class Proprietario:
    proprietarios = []
    def __init__(self, nome, nome_completo, imovel, localizacao):
        self.nome = nome
        self.nome_completo = nome_completo
        self.imovel = imovel
        self.localizao = localizacao
        self.contrato = False
        Proprietario.proprietarios.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.nome_completo} | {self.imovel} | {self.localizao} | {self.contrato}'
    
    def listar_proprietarios():
        print('''''')
        print(f'{"Nome do proprietario".ljust(20)} | {"Nome completo".ljust(20)} | {"Imóvel".ljust(20)} |
        {"Localização".ljust(20)} | {"Cobtrato".ljust(20)}')
        print('-------------------------------------------------------------------------------------')
        for proprietario in Proprietario.proprietarios:
            print(f'{proprietario.nome} | {proprietario.modelo} | {proprietario.estado} | {proprietario.ativo}')
        print('-------------------------------------------------------------------------------------')

    @property
    def contrato(self):
        return '✔️ Contrato' if self.contrato else '❌ Não afirmado' 
       
proprietario_Ricardo = Proprietario('Ricardo', 'Ricardo Brazza', 'Apartamento', 'Edificio José Maria')
proprietario_Roberta = Proprietario('Roberta', 'Roberta Bezera', 'Casa', 'Rua Roberto batata 1190')
proprietario_Lia = Proprietario('Lia', 'Lia Mutsuki', 'Casa', 'Rua Lion Ribeiro 2385')






