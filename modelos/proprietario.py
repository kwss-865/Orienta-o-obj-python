from modelos.especificacao import Especificao

class Proprietario:   
    proprietarios = []
   
    def __init__(self, nome, nome_completo, imovel, localizacao):
        self._nome = nome.upper()
        self._nome_completo = nome_completo.title()
        self._imovel = imovel.upper()
        self._localizacao = localizacao 
        self._especificacao = []
        self._contrato = False
        Proprietario.proprietarios.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._nome_completo} | {self._imovel} | {self._localizacao} | {self.contrato}'

    @classmethod
    def listar_proprietarios(cls):
        print('''
            
            ██████████████████████████████████████████████████████████████████████████████████████████
            █▄─▄█▄─▀█▀─▄█─▄▄─█▄─▄─▀█▄─▄█▄─▄███▄─▄██▀▄─██▄─▄▄▀█▄─▄██▀▄─████▄─█─▄█▄─█▀▀▀█─▄█─▄▄▄▄█─▄▄▄▄█
            ██─███─█▄█─██─██─██─▄─▀██─███─██▀██─███─▀─███─▄─▄██─███─▀─█████─▄▀███─█─█─█─██▄▄▄▄─█▄▄▄▄─█
            ▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▀▄▄▄▄▀▀▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▀▄▄▀▀▀▄▄▀▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀

         ''')
            
        print(f'{"Nome do proprietario".ljust(15)} | {"Nome completo".ljust(20)} | {"Imóvel".ljust(15)} | {"Localização".ljust(25)} | {"Contrato".ljust(18)} | {"Especificacao R$"}')
        print('----------------------------------------------------------------------------------------------------------------------------------')

        for proprietario in cls.proprietarios:
            print(f'{proprietario._nome.ljust(20)} | {proprietario._nome_completo.ljust(20)} | {proprietario._imovel.ljust(15)} | {proprietario._localizacao.ljust(25)} | {proprietario.contrato.ljust(17)} | {str(proprietario.media_especificacao)}')
        print('----------------------------------------------------------------------------------------------------------------------------------')

    @property
    def contrato(self):
        return '✔️ Contrato' if self._contrato else '❌ Não afirmado'
    
    def alterar_estado(self):
        self._contrato = not self._contrato 
    
    def receber_especificao(self, metrosquadrados, preco):
        especificacao = Especificao(metrosquadrados, preco)
        self._especificacao.append(especificacao)
    
    @property
    def media_especificacao(self):
        if not self._especificacao:
            return 0
        soma_dos_precos = sum(especificacao._preco for especificacao in self._especificacao)
        quantidade_imoveis = len(self._especificacao)
        media = round(soma_dos_precos / quantidade_imoveis, 1)
        return media 
        
        