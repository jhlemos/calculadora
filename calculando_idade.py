from datetime import datetime

# Função para calcular a idade
def calcular_idade(data_nascimento):
    hoje = datetime.today()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade

# Entrada do usuário
data_nascimento_str = input("Digite sua data de nascimento (dd/mm/aaaa): ")
data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")

# Calcular e mostrar a idade
idade = calcular_idade(data_nascimento)
print(f"Sua idade é: {idade} anos.")
