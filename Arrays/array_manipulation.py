def array_manipulation(n, queries):
    """
    array_manipulation possui os seguintes parâmetros:
    n - o número de elementos no seu array
    queries - um array bidimensional de consultas, onde
    cada queries[i] contém três inteiros, a, b, e k.
    """
    arr = [0] * n
    for i in queries:
        """
        for j in range(i[0], i[1] + 1):
            arr[j - 1] += i[2]
    return max(arr)"""
        arr[i[0] - 1] += i[2]
        if i[1] != len(arr):
            arr[i[1]] -= i[2]
    
    # A ideia aqui é que a soma só precisa ser calculada para cada "subida" ou "descida"
    # no array, ao invés de ser calculada para cada elemento individual. 
    # Isso é mais fácil de entender se você desenhar um gráfico,
    # mas, em última análise, permite que façamos um único laço para calcular
    # as duas etapas no array, e outro para calcular a altura máxima da etapa.
    # Ainda resta o caso especial em que `arr[i[1]] -= i[2]` não funciona porque 
    # se `i[1] == len(arr)`, adicionar a "descida" à "subida" é errado.
    # Então, basta adicionar uma condicional antes da linha `arr[i[1]] -= i[2]` - linha 54
    max_value = 0
    itk = 0
    print(arr)
    for q in arr:
        itk += q
        if itk > max_value:
            max_value = itk
    return max_value
    
n = 5
queries = [ [1, 2, 100],
            [2, 5, 100],     
            [3, 4, 100]]
print(array_manipulation(n,queries))

"""
1. arr = [0] * n
criamos um array arr de tamanho n, onde todos os elementos são inicialmente 0.
Exemplo: Se n = 5, arr começa como [0, 0, 0, 0, 0].
2. for i in queries:
Este laço percorre cada uma das operações (ou consultas) em queries. Cada consulta i é uma lista de três inteiros [a, b, k].
3. arr[i[0] - 1] += i[2]
Este comando adiciona k ao elemento do array arr na posição a-1. Isso marca o início do incremento no array.
Exemplo: Se i = [1, 2, 100], então arr[0] += 100, o que muda arr para [100, 0, 0, 0, 0].
4. if i[1] != len(arr): arr[i[1]] -= i[2]
Se b não for o último índice do array, este comando subtrai k do elemento arr na posição b. Isso marca o final do incremento no array.
Exemplo: Para i = [1, 2, 100], arr[2] -= 100 (mas como o índice 2 é o limite da operação, arr[2] é subtraído em 100, marcando o fim do incremento).
Resultado: [100, 0, -100, 0, 0].
5. Propósito do Arranjo Inicial
Este arranjo inicial de adição e subtração nos permite aplicar as operações de forma eficiente. Em vez de adicionar k a cada elemento entre a e b (o que seria ineficiente), nós marcamos onde a soma deve começar (arr[a-1] += k) e onde ela deve parar (arr[b] -= k).
6. Cálculo do Valor Máximo
Agora precisamos percorrer o array arr para aplicar essas marcações e encontrar o valor máximo resultante.
itk mantém o valor acumulado enquanto percorremos o array.
max_value é atualizado sempre que encontramos um novo valor acumulado maior que o valor máximo anterior.
7. Exemplo Completo:
Considere n = 5 e queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]].

Operação 1:
[100, 0, -100, 0, 0]
Operação 2:
[100, 100, -100, 0, -100]
Operação 3:
[100, 100, 0, 0, -100]
Final Array:

Percorrendo o array para encontrar o valor máximo:
itk = 100, max_value = 100
itk = 200, max_value = 200 (novo máximo)
itk = 200, max_value = 200
itk = 200, max_value = 200
itk = 100, max_value permanece 200
Resultado:

O valor máximo no array após todas as operações é 200.
"""