# Matrixa

Matrixa is a powerful Python library designed to simplify matrix operations with an easy-to-use API. Whether you need to perform basic tasks like transposition, addition, and subtraction, or more advanced operations like determinant calculation, **Matrixa** is here to assist you.

---

## Features

- **Matrix Initialization**: Easily create matrices of any size with customizable fill values.
- **Element Access**: Get and set values at any position in the matrix.
- **Matrix Transformations**: Perform basic operations like transpose and fill.
- **Advanced Operations**: Calculate determinant, find max/min values, and more.
- **Matrix Arithmetic**: Perform element-wise addition, subtraction, multiplication, and scalar multiplication.

---

## Table of Contents

- [Constructor](#constructor)
- [Matrix Representation](#matrix-representation)
- [Accessing and Modifying Elements](#accessing-and-modifying-elements)
- [Matrix Transformation](#matrix-transformation)
- [Adding and Removing Rows/Columns](#adding-and-removing-rows-or-columns)
- [Matrix Properties](#matrix-properties)
- [Advanced Operations](#advanced-operations)
- [Matrix Arithmetic](#matrix-arithmetic)
- [Usage Examples](#usage-examples)

---

## Constructor

### `__init__(rows: int, cols: int, fill: float = 0)`
- **Description**: Initializes the matrix with specified dimensions and a default fill value.
- **Parameters**:
  - `rows`: Number of rows in the matrix.
  - `cols`: Number of columns in the matrix.
  - `fill`: Default value to fill the matrix (default is 0).

---

## Matrix Representation

### `__repr__()`
- **Description**: Returns a formatted string representation of the matrix for easy printing.

---

## Accessing and Modifying Elements

### `get(row: int, col: int) -> float`
- **Description**: Retrieves the value at a specified position in the matrix.
  
### `set(row: int, col: int, value: float)`
- **Description**: Sets the value at a specified position in the matrix.

---

## Matrix Transformation

### `transpose()`
- **Description**: Transposes the matrix (swaps rows and columns).

### `fill_with(value: float)`
- **Description**: Fills the entire matrix with a single value.

---

## Adding and Removing Rows or Columns

### `add_row(values: list = None)`
- **Description**: Adds a new row to the matrix, filling with zeros if no values are provided.

### `add_col(values: list = None)`
- **Description**: Adds a new column to the matrix, filling with zeros if no values are provided.

### `remove_row(index: int)`
- **Description**: Removes a row at the specified index.

### `remove_col(index: int)`
- **Description**: Removes a column at the specified index.

---

## Matrix Properties

### `is_square() -> bool`
- **Description**: Checks if the matrix is square (rows == columns).

---

## Advanced Operations

### `find_max() -> tuple`
- **Description**: Finds the maximum value in the matrix and its position.

### `find_min() -> tuple`
- **Description**: Finds the minimum value in the matrix and its position.

### `determinant() -> float`
- **Description**: Calculates the determinant of the matrix (square matrices only).

---

## Matrix Arithmetic

### `add_matrix(other)`
- **Description**: Adds another matrix to the current one element-wise.

### `subtract_matrix(other)`
- **Description**: Subtracts another matrix from the current one element-wise.

### `multiply_matrix(other)`
- **Description**: Multiplies the current matrix with another matrix.

### `scalar_multiply(scalar: float)`
- **Description**: Multiplies the matrix by a scalar value.

---

## Usage Examples

```python
# Create a 2x3 matrix, filled with ones
matrix = Matrixa(2, 3, fill=1)

# Set a value at a specific position
matrix.set(0, 0, 5)

# Print the matrix
print(matrix)
