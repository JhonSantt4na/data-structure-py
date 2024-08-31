"""
Você recebeu um array contendo números.
Encontre e retorne a maior soma em um subarray contíguo dentro do array de entrada.

Exemplo 1
arr= [1, 2, 3, -4, 6]
A maior soma é '8', que é a soma de todos os elementos do array.

Exemplo 2
arr = [1, 2, -5, -4, 1, 6]
A maior soma é '7', que é a soma dos dois últimos elementos do array.
"""

def max_sum_subarray(arr):
    max_so_far = 0
    max_ending_here = 0
    for i in range(0, len(arr)):
        max_ending_here += arr[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

arr = [1, 2, 3, -4, 6]
print(str(max_sum_subarray(arr)))
