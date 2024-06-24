import numpy as np

def input_matrix():
    n = int(input("Masukkan ukuran matriks (n x n): "))
    matrix = []
    print("Masukkan elemen-elemen matriks:")
    for i in range(n):
        row = list(map(float, input(f"Masukkan elemen baris {i+1} (pisahkan dengan spasi): ").split()))
        matrix.append(row)
    return np.array(matrix)

def calculate_determinant(matrix):
    return np.linalg.det(matrix)

# Meminta input matriks dari pengguna
matrix = input_matrix()

# Menghitung determinan matriks
det = calculate_determinant(matrix)

# Menampilkan hasil
print(f"Determinannya adalah: {det}")