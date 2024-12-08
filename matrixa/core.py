class Matrixa:
    def __init__(self, rows: int, cols: int, fill: float = 0):
        """
        initialize the matrix with given dimensions and a default fill value.
        :param rows: number of rows in the matrix.
        :param cols: number of columns in the matrix.
        :param fill: default value to fill the matrix (default 0).
        
        inicializa a matriz com dimensões dadas e um valor padrão para preenchimento.
        :param rows: numero de linhas na matriz.
        :param cols: numero de colunas na matriz.
        :param fill: valor padrao para preencher a matriz (padrao 0).
        """
        if rows <= 0 or cols <= 0:
            raise ValueError("matrix dimensions must be positive integers.")
        self.rows = rows
        self.cols = cols
        self.data = [[fill for _ in range(cols)] for _ in range(rows)]

    def __repr__(self):
        #function to show a formatted matrix when printed
        #funcao para mostrar uma matrix formatada quando printar
        max_len = max(len(str(item)) for row in self.data for item in row)
        
        formatted_rows = [
            " ".join(f"{item:>{max_len}}" for item in row) for row in self.data
        ]
        
        return "\n".join(formatted_rows)

    def get(self, row: int, col: int) -> float:
        """
        get the value at a specific position in the matrix.
        :param row: row index.
        :param col: column index.
        :return: value at the specified position.

        obtem o valor de uma posição da matriz.
        :param row: linha da matriz.
        :param col: coluna da matriz.
        :return: valor na posição especificada.
        """
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise IndexError("matrix indices out of range.")
        return self.data[row][col]

    def set(self, row: int, col: int, value: float):
        """
        set the value at a specific position in the matrix.
        :param row: row index.
        :param col: column index.
        :param value: value to set.

        define o valor em uma posição específica da matriz.
        :param row: linha da matriz.
        :param col: coluna da matriz.
        :param value: valor desejado a ser definido.
        """
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise IndexError("matrix indices out of range.")
        self.data[row][col] = value

    def fill_with(self, value: float):
        """
        fill the entire matrix with a specific value.
        :param value: Value to fill the matrix with.

        preenche toda a matriz com um valor único.
        :param value: valor desejado para preencher a matriz.
        """
        for row in range(self.rows):
            for col in range(self.cols):
                self.data[row][col] = value

    def add_row(self, values=None):
        """
        add a new row to the matrix. If values are not provided, fill with 0.
        :param values: list of values for the new row.
        
        adiciona uma nova linha à matriz. Se os valores não forem fornecidos, preenche com 0.
        :param values: lista de valores para a nova linha.
        """
        if values is None:
            values = [0] * self.cols
        elif len(values) != self.cols:
            raise ValueError("Length of values must match the number of columns.")
        self.data.append(values)
        self.rows += 1

    def add_col(self, values=None):
        """
        add a new column to the matrix. If values are not provided, fill with 0.
        :param values: list of values for the new column.
        
        adiciona uma nova coluna à matriz. Se os valores não forem fornecidos, preenche com 0.
        :param values: lista de valores para a nova coluna.
        """
        if values is None:
            values = [0] * self.rows
        elif len(values) != self.rows:
            raise ValueError("Length of values must match the number of rows.")
        for i in range(self.rows):
            self.data[i].append(values[i])
        self.cols += 1

    def remove_row(self, index: int):
        """
        remove a row at a specific index.
        :param index: index of the row to remove.
        
        remove uma linha em um índice específico.
        :param index: indice da linha a ser removida.
        """
        if not (0 <= index < self.rows):
            raise IndexError("Row index out of range.")
        self.data.pop(index)
        self.rows -= 1

    def remove_col(self, index: int):
        """
        remove a column at a specific index.
        :param index: index of the column to remove.

        remove uma coluna em um índice específico.
        :param index: índice da coluna a ser removida.
        """
        if not (0 <= index < self.cols):
            raise IndexError("Column index out of range.")
        for row in self.data:
            row.pop(index)
        self.cols -= 1

    def transpose(self):
        """
        transpose the matrix (swap rows and columns).
        transpor a matriz (trocar linhas e colunas).
        """
        self.data = [list(row) for row in zip(*self.data)]
        self.rows, self.cols = self.cols, self.rows

    def is_square(self) -> bool:
        """
        check if the matrix is square (rows == cols).
        :return: True if the matrix is square, False otherwise.

        verifica se a matriz é quadrada (linhas == colunas).
        :return: True se a matriz for quadrada, False caso contrário.
        """
        return self.rows == self.cols
    
    def from_list(self, input_list: list):
        """
        fills the matrix with the values provided in a one-dimensional list.
        :param input_list: list containing the elements to be filled into the matrix.

        preenche a matriz com os valores fornecidos em uma lista unidimensional.
        :param input_list: lista contendo os elementos a serem preenchidos na matriz.
        """
        if len(input_list) != self.rows * self.cols:
            raise ValueError("the number of elements in the list does not match the size of the matrix.")
        
        idx = 0
        for row in range(self.rows):
            for col in range(self.cols):
                self.data[row][col] = input_list[idx]
                idx += 1

    def find_max(self):
        """
        find the maximum value in the matrix and its position.
        :return: a tuple with the maximum value and its position (row, col).

        encontra o valor máximo na matriz e sua posição.
        :return: uma tupla com o valor máximo e sua posição (linha, coluna).
        """

        max_value = self.data[0][0]
        max_pos = (0, 0)
        for row in range(self.rows):
            for col in range(self.cols):
                if self.data[row][col] > max_value:
                    max_value = self.data[row][col]
                    max_pos = (row, col)
        return max_value, max_pos
    
    def find_min(self):
        """
        find the minimum value in the matrix and its position.
        :return: a tuple with the minimum value and its position (row, col).

        encontra o valor mínimo na matriz e sua posição.
        :return: uma tupla com o valor mínimo e sua posição (linha, coluna).
        """

        min_value = self.data[0][0]
        min_pos = (0, 0)
        for row in range(self.rows):
            for col in range(self.cols):
                if self.data[row][col] < min_value:
                    min_value = self.data[row][col]
                    min_pos = (row, col)
        return min_value, min_pos
    
    def add_matrix(self, other):
        """
        add another matrix to the current matrix, element-wise.
        :param other: another matrix instance with the same dimensions.
        :return: a new matrix with the result.

        adiciona outra matriz à matriz atual, elemento por elemento.
        :param other: outra matrix com as mesmas dimensões.
        :return: uma nova matrix com o resultado.
        """

        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("matrices must have the same dimensions for addition.")
        result = Matrixa(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                result.data[row][col] = self.data[row][col] + other.data[row][col]
        return result
    
    def subtract_matrix(self, other):
        """
        subtract another matrix from the current matrix, element-wise.
        :param other: another matrix instance with the same dimensions.
        :return: a new matrix with the result.

        subtrai outra matriz da matriz atual, elemento por elemento.
        :param other: outra matriz com as mesmas dimensões.
        :return: uma nova matriz com o resultado.
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("matrices must have the same dimensions for subtraction")

        result = Matrixa(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                result.data[row][col] = self.data[row][col] - other.data[row][col]
        return result
    
    def multiply_matrix(self, other):
        """
        multiply the current matrix by another matrix.
        :param other: another matrix instance with compatible dimensions (columns of the first = rows of the second).
        :return: a new matrix with the product.

        multiplica a matriz atual por outra matriz.
        :param other: outra matriz com dimensões compatíveis (colunas da primeira = linhas da segunda).
        :return: uma nova matriz com o produto.
        """
        if self.cols != other.rows:
            raise ValueError("number of columns of the first matrix must equal the number of rows of the second matrix.")
        
        result = Matrixa(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                result.data[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
        return result
    
    def scalar_multiply(self, scalar: float):
        """
        multiply the current matrix by a scalar value.
        :param scalar: a numerical value to multiply each element of the matrix.
        :return: a new matrix with the result.

        multiplica a matriz atual por um valor escalar.
        :param scalar: um valor numérico para multiplicar cada elemento da matriz.
        :return: uma nova matriz com o resultado.
        """
        result = Matrixa(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                result.data[row][col] = self.data[row][col] * scalar
        return result
    
    def determinant(self):
        """
        calculate the determinant of the matrix (only for square matrices).
        :return: the determinant value as a float.

        calcula o determinante da matriz (somente para matrizes quadradas).
        :return: o valor do determinante como um float.
        """
        if not self.is_square():
            raise ValueError("determinant can only be calculated for square matrices.")

        def _determinant_recursive(data):
            """
            helper function to calculate the determinant recursively.
            :param data: a list of lists representing a square matrix.
            :return: the determinant value.

            função auxiliar para calcular o determinante recursivamente.
            :param data: uma lista de listas representando uma matriz quadrada.
            :return: o valor do determinante.
            """
            if len(data) == 1:
                return data[0][0]
            if len(data) == 2:
                return data[0][0] * data[1][1] - data[0][1] * data[1][0]
            
            det = 0
            for col in range(len(data)):
                minor = [row[:col] + row[col+1:] for row in data[1:]]
                det += ((-1) ** col) * data[0][col] * _determinant_recursive(minor)
            return det

        return _determinant_recursive(self.data)