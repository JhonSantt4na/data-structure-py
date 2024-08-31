"""
Uma operação de rotação à esquerda em um array de tamanho 'n'
desloca cada um dos elementos do array 1 unidade para a esquerda.
Por exemplo, se 2 rotações à esquerda forem realizadas no array [1, 2, 3, 4, 5],
então o array se tornaria [3, 4, 5, 1, 2].

Dado um array de n inteiros e um número, 'd', execute 'd' rotações à esquerda no array.
Então imprima o array atualizado como uma única linha de inteiros separados por espaços.
"""
def left_rotation(a, d):
    return a[d:] + a[:d]

a = [1, 2, 3, 4, 5]
print(left_rotation(a, 4))

