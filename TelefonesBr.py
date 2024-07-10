import re  # Importa o módulo re para trabalhar com expressões regulares

class TelefonesBr:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Número incorreto!")  # Lança um erro se o número não for válido

    def __str__(self):
        return self.format_numero()  # Retorna uma representação formatada do número de telefone

    def valida_telefone(self, telefone):
        padrao = "(\+\d{2})?(\d{2})(\d{4,5})(\d{4})"  # Define o padrão de expressão regular para validar o telefone
        resposta = re.findall(padrao, telefone)  # Busca pelo padrão no número de telefone
        if resposta:
            return True  # Retorna True se o número corresponder ao padrão
        else:
            return False  # Retorna False se o número não corresponder ao padrão

    def format_numero(self):
        padrao = "(\+\d{2})?(\d{2})(\d{4,5})(\d{4})"  # Define o padrão de expressão regular para formatar o número
        resposta = re.search(padrao, self.numero)  # Procura pelo padrão no número de telefone
        numero_formatado = "+{}({}){}-{}".format(
            resposta.group(1) if resposta.group(1) else "55",  # Captura o código de país, se presente, senão assume 55 (Brasil)
            resposta.group(2),  # Captura o DDD
            resposta.group(3),  # Captura a parte central do número
            resposta.group(4)   # Captura os últimos dígitos do número
        )
        return numero_formatado  # Retorna o número formatado

# Exemplo de uso:
numero_telefone = "+5511991234567"  # Número de telefone a ser validado e formatado
telefone = TelefonesBr(numero_telefone)  # Cria uma instância da classe TelefonesBr com o número de telefone
print("Número de telefone formatado:", telefone)  # Imprime o número de telefone formatado
