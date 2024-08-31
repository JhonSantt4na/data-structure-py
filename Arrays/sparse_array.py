"""
Há uma coleção de strings de entrada e uma coleção de strings de consulta.
Para cada string de consulta, determine quantas vezes ela ocorre na lista de strings de entrada.

Exemplo: dado uma string de entrada = ['ab', 'ab', 'abc'] e
queries = ['ab',' abc', 'bc'] encontramos 2 instâncias de 'ab',
1 de 'abc' e 0 de 'bc'. Para cada consulta, adicionamos um elemento ao nosso array de retorno
results = [2, 1, 0]

Formato de entrada

A primeira linha contém um inteiro 'n', o tamanho das strings.
Cada uma das próximas 'n' linhas contém uma string 'strings[i]'.
A próxima linha contém 'q', o tamanho das consultas.
Cada uma das próximas 'q' linhas contém uma string 'q[i]'.
"""
def matching_strings(strings, queries):
    results = []
    for i in range(len(queries)):
        count = 0
        for j in range(len(strings)):
            if strings[j] == queries[i]:
               count += 1
        results.append(count)
    return results

strings = ['ab', 'ab', 'abc']
queries = ['ab','abc', 'bc']

print(matching_strings(strings, queries))