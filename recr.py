from datetime import datetime

# Função para calcular o número de dias que a pessoa está viva
def dias_vivo(data_nascimento):
    hoje = datetime.today()
    delta = hoje - data_nascimento
    return delta.days

# Função para calcular os dias restantes até o próximo aniversário
def dias_para_aniversario(data_nascimento):
    hoje = datetime.today()
    proximo_aniversario = datetime(hoje.year, data_nascimento.month, data_nascimento.day)
    
    # Se o aniversário já passou neste ano, considerar o próximo ano
    if proximo_aniversario < hoje:
        proximo_aniversario = datetime(hoje.year + 1, data_nascimento.month, data_nascimento.day)
    
    delta = proximo_aniversario - hoje
    return delta.days

# Solicitar a data de nascimento
data_nascimento_str = input("Digite sua data de nascimento (dd/mm/aaaa): ")
data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")

# Calcular os dias vividos e os dias para o próximo aniversário
dias_vividos = dias_vivo(data_nascimento)
dias_ate_aniversario = dias_para_aniversario(data_nascimento)

# Exibir os resultados
print(f"\nVocê está vivo há {dias_vividos} dias.")
print(f"Faltam {dias_ate_aniversario} dias para o seu próximo aniversário.")
