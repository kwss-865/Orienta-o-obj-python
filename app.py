from modelos.proprietario import Proprietario

proprietario_Ricardo = Proprietario('Ricardo', 'Ricardo Brazza', 'Apartamento', 'Edificio José Maria')
proprietario_Roberta = Proprietario('Roberta', 'Roberta Bezera', 'Casa', 'Rua Roberto batata 1190')
proprietario_Lia = Proprietario('Lia', 'Lia Mutsuki', 'Casa', 'Rua Lion Ribeiro 2385')

proprietario_Lia.alterar_estado()
proprietario_Ricardo.receber_especificao('70', 150.000)
proprietario_Ricardo.receber_especificao('150', 300.000)
proprietario_Ricardo.receber_especificao('55', 100.000)

def main():
    Proprietario.listar_proprietarios() 

if __name__ == '__main__':
    main()