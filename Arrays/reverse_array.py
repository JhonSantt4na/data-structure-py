"""
Dado um array de 'A' de 'N' inteiros, imprima cada elemento em ordem reversa
como uma única linha de inteiros separados por espaços.

Exemplo:
Entrada = 1 4 3 2
Saída = 2 3 4 1
"""

# Inverta o array

# Método 1
# Loop for
def reverseArray_1(a):
    b = []
    for i in a:
        b.insert(0, i)
    return b


# Método 2
# Copia a lista antes de revertê-la
def reverseArray_2(a):
    return a[::-1]

# Método 3
# A maneira mais rápida de reverter uma lista longa
def reverseArray_3(a):
    a = a.reverse()
    return a

a = [1, 4, 3, 2]
print (reverseArray_1(a))
print (reverseArray_2(a))

reverseArray_3(a)
print(a)