#Exercise10: Verifica Matrice quadrata

def is_identity(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i == j:
                if matrix[i][j] != 1:
                    return False
            else:
                if matrix[i][j] != 0:
                    return False
    return True

def is_null(matrix):
    for row in matrix:
        for element in row:
            if element != 0:
                return False
    return True

def is_lower_triangular(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            if matrix[i][j] != 0:
                return False
    return True

def main():
    # Esempio di matrice quadrata 3x3
    m1 = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]

    print("Matrice Identità:", is_identity(m1))
    print("Matrice Nulla:", is_null(m1))
    print("Matrice Triangolare Inferiore:", is_lower_triangular(m1))

if __name__ == "__main__":
    main()