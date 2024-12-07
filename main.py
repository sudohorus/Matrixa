from matrixa.core import Matrixa

#criar uma matriz 3x3 com valores padrão 0
#create a 3x3 matrix with default value 0
matrix = Matrixa(3, 3)
print(matrix)

print()

#configurar o valor na posição (1,1) para 5
#set the value at position (1,1) to 5
matrix.set(1, 1, 5)
print(matrix)

print()

#obter o valor na posição (1,1)
#get the value at position (1,1)
value = matrix.get(1, 1)
print(f"{value}\n")

#preencher toda a matriz com o valor 7
#fill the entire matrix with the value 7
matrix.fill_with(7)
print(matrix)

print()

#adicionar uma nova linha com valores [1, 2, 3]
#add a new row with values [1, 2, 3]
matrix.add_row([1, 2, 3])
print(matrix)

print()

#adicionar uma nova coluna com valores [4, 5, 6, 7]
#add a new column with values [4, 5, 6, 7]
matrix.add_col([4, 5, 6, 7])
print(matrix)

print()

#remover a terceira linha (índice 2)
#remove the third row (index 2)
matrix.remove_row(2)
print(matrix)

print()

#remover a segunda coluna (índice 1)
#remove the second column (index 1)
matrix.remove_col(1)
print(matrix)

print()

#transpor a matriz
#transpose the matrix
matrix.transpose()
print(matrix)

print()

#verificar se a matriz é quadrada
#check if the matrix is square
is_square = matrix.is_square()
print(f"{'Sim/Yes' if is_square else 'Não/No'}\n")

#preencher a matriz com uma lista de valores [1, 2, 3, 4, 5, 6]
#fill the matrix with a list of values [1, 2, 3, 4, 5, 6]
matrixList = Matrixa(2, 3)
matrixList.from_list([1, 2, 3, 4, 5, 6])
print(matrixList)
