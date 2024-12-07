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
