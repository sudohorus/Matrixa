from matrixa.core import Matrixa

mat1 = Matrixa(3, 3)
mat2 = Matrixa(3, 3)

mat1.data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

mat2.data = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print(mat1.subtract_matrix(mat2), "\n")
print(mat1.multiply_matrix(mat2), "\n")
print(mat1.scalar_multiply(2), "\n")
print(mat1.determinant(), "\n")
