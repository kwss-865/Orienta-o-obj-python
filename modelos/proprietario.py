class Proprietario:
    nome = ''
    nome_completo = ''
    imovel = ''
    localizao = ''
    contrato = False
    
proprietario_Ricardo = Proprietario()
proprietario_Roberta = Proprietario()
proprietario_Lia = Proprietario()

proprietario_Roberta.nome_completo = 'Roberta Brazza'
proprietario_Ricardo.nome_completo = 'Ricardo Bezera'

proprietarios = [proprietario_Ricardo, proprietario_Roberta, proprietario_Lia]

print(proprietarios\n)
print(proprietario_Roberta\n)
print(dir(proprietarios))