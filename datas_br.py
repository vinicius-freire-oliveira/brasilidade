from datetime import datetime, timedelta  # Importa as classes datetime e timedelta do módulo datetime

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()  # Inicializa o momento de cadastro como o datetime atual

    def __str__(self):
        return self.format_data()  # Retorna uma representação formatada da data de cadastro
    
    def mes_cadastro(self):
        # Retorna o mês do cadastro com base no atributo moment_cadastro
        meses_do_ano = [
            "janeiro", "fevereiro", "março", 
            "abril", "maio", "junho", "julho", 
            "agosto", "setembro", "outubro", 
            "novembro", "dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month - 1  # Obtém o índice do mês
        return meses_do_ano[mes_cadastro]  # Retorna o nome do mês
    
    def dia_semana(self):
        # Retorna o dia da semana do cadastro com base no atributo moment_cadastro
        dia_semana_lista = [
            "segunda", "terça", "quarta", 
            "quinta", "sexta", "sábado", 
            "domingo"
        ]
        dia_semana = self.momento_cadastro.weekday()  # Obtém o dia da semana (0 a 6)
        return dia_semana_lista[dia_semana]  # Retorna o nome do dia da semana
    
    def format_data(self):
        # Formata a data de cadastro conforme o padrão especificado
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada  # Retorna a data formatada
    
    def tempo_cadastro(self):
        # Calcula o tempo de cadastro até 30 dias após a data atual
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return tempo_cadastro  # Retorna o tempo de cadastro

# Exemplo de uso:
data_atual = DatasBr()

print("Data de cadastro:", data_atual)
print("Mês do cadastro:", data_atual.mes_cadastro())
print("Dia da semana do cadastro:", data_atual.dia_semana())
print("Tempo de cadastro:", data_atual.tempo_cadastro())
