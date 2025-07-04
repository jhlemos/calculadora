from datetime import datetime

# Função para calcular o número de dias que a pessoa está viva
def dias_vivo(data_nascimento):
    hoje = datetime.today()
    delta = hoje - data_nascimento
    return delta.days

# Função para calcular a idade (anos)
def calcular_idade(data_nascimento):
    hoje = datetime.today()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade

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

# Calcular os resultados
dias_vividos = dias_vivo(data_nascimento)
idade = calcular_idade(data_nascimento)
dias_ate_aniversario = dias_para_aniversario(data_nascimento)

# Exibir os resultados
print(f"\nVocê tem {idade} anos.")
print(f"Você está vivo há {dias_vividos} dias.")
print(f"Faltam {dias_ate_aniversario} dias para o seu próximo aniversário.")
.