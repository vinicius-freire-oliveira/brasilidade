from validate_docbr import CPF, CNPJ  # Importa as classes CPF e CNPJ do módulo validate_docbr

class Documento:

    @staticmethod
    def cria_documento(documento):
        # Método estático que cria um objeto de DocCpf ou DocCnpj com base no tamanho do documento
        if len(documento) == 11:
            return DocCpf(documento)  # Retorna um objeto DocCpf se o documento tem 11 dígitos
        elif len(documento) == 14:
            return DocCnpj(documento)  # Retorna um objeto DocCnpj se o documento tem 14 dígitos
        else:
            raise ValueError ("Quantidade de dígitos está incorreta!!")  # Levanta um erro se o tamanho do documento não é válido
        
class DocCpf:
    def __init__(self, documento):
        # Inicializa o objeto DocCpf com um CPF válido
        if self.valida(documento):
            self.cpf = documento  # Atribui o CPF ao objeto se for válido
        else:
            raise ValueError("Cpf inválido")  # Levanta um erro se o CPF não for válido
    
    def __str__(self):
        # Retorna uma representação formatada do CPF
        return self.format()
    
    def valida(self, documento):
        # Valida se o CPF é válido utilizando a classe CPF do módulo validate_docbr
        validador = CPF()
        return validador.validate(documento)
        
    def format(self):
        # Formata o CPF com máscara utilizando a classe CPF do módulo validate_docbr
        mascara = CPF()
        return mascara.mask(self.cpf)
    
class DocCnpj:
    def __init__(self, documento):
        # Inicializa o objeto DocCnpj com um CNPJ válido
        if self.valida(documento):
            self.cnpj = documento  # Atribui o CNPJ ao objeto se for válido
        else:
            raise ValueError("Cnpj inválido!!")  # Levanta um erro se o CNPJ não for válido
        
    def __str__(self):
        # Retorna uma representação formatada do CNPJ
        return self.format()
    
    def valida(self, documento):
        # Valida se o CNPJ é válido utilizando a classe CNPJ do módulo validate_docbr
        mascara = CNPJ()
        return mascara.validate(documento)
    
    def format(self):
        # Formata o CNPJ com máscara utilizando a classe CNPJ do módulo validate_docbr
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

# Exemplo de uso:
documento = input("Digite o CPF ou CNPJ: ")
doc = Documento.cria_documento(documento)

# Verificar o tipo de documento e imprimir o valor formatado
if isinstance(doc, DocCpf):
    print("CPF formatado:", doc)
elif isinstance(doc, DocCnpj):
    print("CNPJ formatado:", doc)
