import requests

class BuscaEndereco:
    def __init__(self, cep):
        # Verifica se o CEP é válido ao inicializar a instância
        if self.cep_e_valido(str(cep)):
            self.cep = str(cep)
        else:
            raise ValueError("CEP inválido!!")
    
    def __str__(self):
        # Retorna o CEP formatado quando a instância é convertida para string
        return self.format_cep()
    
    def cep_e_valido(self, cep):
        # Verifica se o CEP possui 8 caracteres
        if len(cep) == 8:
            return True
        else:
            return False
    
    def format_cep(self):
        # Formata o CEP no formato 12345-678
        return "{}-{}".format(self.cep[:5], self.cep[5:])
    
    def acessa_via_cep(self):
        # Acessa a API ViaCEP para obter informações do CEP
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        dados = r.json()
        # Retorna uma tupla com bairro, localidade e UF
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )

# Exemplo de uso:
cep = input("Digite o CEP: ")
endereco = BuscaEndereco(cep)
bairro, localidade, uf = endereco.acessa_via_cep()

print("Bairro:", bairro)
print("Localidade:", localidade)
print("UF:", uf)
