class Proprietario:
    def __init__(self, nome, nome_completo, imovel, localizacao):
        self.nome = nome
        self.nome_completo = nome_completo
        self.imovel = imovel
        self.localizao = localizacao
        self.contrato = False
    
    def __str__(self):
        return f'{self.nome} | {self.nome_completo} | {self.imovel} | {self.localizao} | {self.contrato}'
    
proprietario_Ricardo = Proprietario('Ricardo', 'Ricardo Brazza', 'Apartamento', 'Edificio José Maria')
proprietario_Roberta = Proprietario('Roberta', 'Roberta Bezera', 'Casa', 'Rua Roberto batata 1190')
proprietario_Lia = Proprietario('Lia', 'Lia Mutsuki', 'Casa', 'Rua Lion Ribeiro 2385')

proprietarios = [proprietario_Ricardo, proprietario_Roberta, proprietario_Lia]

print(proprietario_Ricardo)
print(proprietario_Lia)




