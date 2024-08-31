linhas = 5
b = 0
for i in range(linhas, 0, -1):
   b += 1
   for j in range(1,i+1):
      print(b, end=' ')
   print('\r')

# 1 1 1
# 2 2
# 3


"""
1. linhas = 5
define a variável linhas como 5. Isso significa que o triângulo terá 5 linhas.

2. b = 0
Inicialmente, a variável b é definida como 0. Ela vai ser usada para controlar o número que será impresso em cada linha.

3. for i in range(linhas, 0, -1):
Este é o primeiro laço for, que vai controlar o número de linhas. A função range(linhas, 0, -1) cria uma sequência que começa em 5 e vai até 1 (inclusive), decrementando de 1 em 1. Ou seja, i vai assumir os valores 5, 4, 3, 2 e 1 em cada iteração.

4. b += 1
Dentro do laço, a variável b é incrementada em 1 a cada nova linha. Isso significa que b começará em 1 na primeira linha, será 2 na segunda linha, e assim por diante.

5. for j in range(1, i + 1):
Este é o segundo laço for, que controla quantas vezes o número b será impresso em cada linha. A função range(1, i + 1) cria uma sequência de números que começa em 1 e vai até i (incluindo i). Portanto, na primeira linha, o número b será impresso 5 vezes, na segunda linha 4 vezes, e assim por diante.

6. print(b, end=' ')
Este comando imprime o valor de b na mesma linha, seguido por um espaço (end=' ' evita que o print pule para a próxima linha automaticamente).

7. print('\r')
Este comando serve para mover o cursor para a próxima linha após todos os números de uma linha terem sido impressos. O \r faz o retorno do cursor ao início da linha (equivalente a print('') aqui), preparando a próxima linha para impressão.
"""