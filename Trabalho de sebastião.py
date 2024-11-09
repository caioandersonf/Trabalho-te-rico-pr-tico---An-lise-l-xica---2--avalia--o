import pandas as pd
import re

# Expressão regular para reconhecer os formatos de índices de datasets do pandas
regex = r"\[\-?\d+\]|\['[^']+'\]|\[\"[^\"]+\"\]|\[\-?\d+:\-?\d+\]|\['[^']+':'[^']+'\]|\[\"[^\"]+\":\"[^\"]+\"\]"

# Função para verificar se o índice é válido
def verifica_indice(cadeia):
    return bool(re.fullmatch(regex, cadeia))

# Exemplo de dataset
data = {
    "Date": ["2020-04-26", "2020-04-26", "2020-04-26"],
    "State": ["Andaman and Nicobar Islands", "Andhra Pradesh", "Andhra Pradesh"],
    "District": ["Unknown", "Anantapur", "Chittoor"],
    "Confirmed": [33, 53, 73],
    "Recovered": [11, 14, 13],
    "Deceased": [0, 4, 0],
    "Other": [0, 0, 0],
    "Tested": [None, None, None]
}

# Criando o DataFrame
df = pd.DataFrame(data)

# Lista de exemplos de índices para testar
exemplos_indices = ["[0]", "['Date']", '["New Column"]', "[0:5]", "['Data':'State']", '["District":"Tested"]', "[invalid]"]

# Verificando se cada índice é válido e exibindo o resultado
resultados = {indice: verifica_indice(indice) for indice in exemplos_indices}

# Exibindo os resultados
for indice, valido in resultados.items():
    print(f"{indice}: {'Válido' if valido else 'Inválido'}")
