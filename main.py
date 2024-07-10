#from cpf_cnpj import Documento  # Importa a classe Documento para lidar com CPFs e CNPJs
#from validate_docbr import CNPJ  # Importa a classe CNPJ do módulo validate_docbr
#from TelefonesBr import TelefonesBr  # Importa a classe TelefonesBr para lidar com números de telefone
#import re  # Importa o módulo re para trabalhar com expressões regulares
#from datetime import datetime, timedelta  # Importa datetime e timedelta para lidar com datas e horários
#from datas_br import DatasBr  # Importa a classe DatasBr para lidar com datas formatadas
from acesso_cep import BuscaEndereco  # Importa a classe BuscaEndereco para buscar informações de CEP

# Comentários das linhas de código originalmente presentes:

#cpf_um = "02892041677"
#print(cpf_um)
#exemplo_cnpj = "35379838000112"
#exemplo_cpf = "11111111112"
#cnpj = CNPJ()
#print(cnpj.validate(exemplo_cnpj))
#documento = Documento.cria_documento(cpf_um)
#print(documento)

#telefone = "552126481234"
#telefone_objeto = TelefonesBr(telefone)

#print(telefone_objeto)

#hoje = DatasBr()
#print(hoje.tempo_cadastro())

cep = "01001000"  # Define o CEP que deseja consultar
objeto_cep = BuscaEndereco(cep)  # Cria um objeto BuscaEndereco com o CEP especificado

#r = requests.get("https://viacep.com.br/ws/01001000/json/")
#print(type(r.text))

bairro, cidade, uf = objeto_cep.acessa_via_cep()  # Chama o método acessa_via_cep para obter bairro, cidade e UF

print(bairro, cidade, uf)  # Imprime as informações obtidas: bairro, cidade e UF
