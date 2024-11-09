Trabalho teórico-prático - Análise léxica - 2ª avaliação

Grupo composto por: Anthony Anderson Freitas da Silva, Caio Anderson Bezerra Fernandes, Joao Victor Paiva Maia e Samuel Lima Souza

A expressão regular foi definida da seguinte forma

Índice numérico: reconhece números inteiros, positivos ou negativos, entre colchetes.

Exemplo: [0], [10], [-2]
Regex: \[\-?\d+\]
Índice por nome de coluna: aceita strings entre aspas simples ou duplas, incluindo espaços.

Exemplo: ['Date'], ["New Column"]
Regex: \['[^']+'\]|\["[^"]+"\]
Intervalo numérico: aceita intervalos de dois números inteiros (positivos ou negativos) separados por :.

Exemplo: [0:5], [-1:-5]
Regex: \[\-?\d+:\-?\d+\]
Intervalo de colunas por nome: aceita nomes entre aspas simples ou duplas, separados por :.

Exemplo: ['Data':'State'], ["District":"Tested"]
Regex: \['[^']+':'[^']+'\]|\["[^"]+":"[^"]+"\]
Combinando todos esses padrões, nossa expressão regular final será:

\[\-?\d+\]|\['[^']+'\]|\["[^"]+"\]|\[\-?\d+:\-?\d+\]|\['[^']+':'[^']+'\]|\["[^"]+":"[^"]+"\]

Agora o código funciona assim:

Função verifica_indice: ela usa a expressão regular pra poder verificar se o valor informado é igual a algum dos valores validos com base na formula passada.

Teste com lista de exemplos: usamos uma lista de exemplos de índices para verificar quais são válidos ou inválidos.
