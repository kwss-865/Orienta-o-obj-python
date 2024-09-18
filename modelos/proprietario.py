class Proprietario:
    proprietarios = []
   
    def __init__(self, nome, nome_completo, imovel, localizacao):
        self._nome = nome.upper()
        self._nome_completo = nome_completo.title()
        self._imovel = imovel.upper()
        self._localizacao = localizacao 
        self._contrato = False
        Proprietario.proprietarios.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._nome_completo} | {self._imovel} | {self._localizacao} | {self.contrato}'

    @classmethod
    def listar_proprietarios():
        print('''
            
            ██████████████████████████████████████████████████████████████████████████████████████████
            █▄─▄█▄─▀█▀─▄█─▄▄─█▄─▄─▀█▄─▄█▄─▄███▄─▄██▀▄─██▄─▄▄▀█▄─▄██▀▄─████▄─█─▄█▄─█▀▀▀█─▄█─▄▄▄▄█─▄▄▄▄█
            ██─███─█▄█─██─██─██─▄─▀██─███─██▀██─███─▀─███─▄─▄██─███─▀─█████─▄▀███─█─█─█─██▄▄▄▄─█▄▄▄▄─█
            ▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▀▄▄▄▄▀▀▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▀▄▄▀▀▀▄▄▀▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀

         ''')
            
        print(f'{"Nome do proprietario".ljust(15)} | {"Nome completo".ljust(20)} | {"Imóvel".ljust(15)} | {"Localização".ljust(25)} | {"Contrato"}')
        print('------------------------------------------------------------------------------------------------------------')

        for proprietario in Proprietario.proprietarios:
            print(f'{proprietario._nome.ljust(20)} | {proprietario._nome_completo.ljust(20)} | {proprietario._imovel.ljust(15)} | {proprietario._localizacao.ljust(25)} | {proprietario.contrato}')
        print('------------------------------------------------------------------------------------------------------------')

    @property
    def contrato(self):
        return '✔️ Contrato' if self._contrato else '❌ Não afirmado'
    
    def alterar_estado(self):
        self._contrato = not self._contrato 