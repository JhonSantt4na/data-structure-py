linhas = 6
for i in range(linhas):
   for j in range(i):
      print(i, end=" ")
   print('')

# 1
# 2 2
# 3 3 3

"""
1. rows = 6
Aqui, você define a variável rows (linhas) como 6. Isso significa que o triângulo terá 6 linhas.

2. for i in range(rows):
Esse é um laço for que vai de 0 até 5 (ou seja, range(rows) vai gerar os números 0, 1, 2, 3, 4 e 5). A variável i vai assumir esses valores em cada iteração do laço.

3. for j in range(i):
Dentro do primeiro laço, temos um segundo laço for. Esse laço vai de 0 até i-1. Ou seja, ele depende do valor de i. Por exemplo:

Quando i = 1, j vai de 0 até 0 (apenas uma iteração).
Quando i = 2, j vai de 0 até 1 (duas iterações).
E assim por diante.
4. print("*", end=" ")
Esse comando imprime um asterisco (*) na mesma linha, porque usamos end=" " para evitar a quebra de linha automática que ocorre após o print por padrão. Ele também adiciona um espaço entre os asteriscos.

5. print('')
Após o laço j, temos esse print(''), que serve para mover o cursor para a próxima linha. Isso faz com que o próximo conjunto de asteriscos seja impresso na linha seguinte, criando o formato de triângulo.
"""