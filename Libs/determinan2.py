import numpy as np

# Mendefinisikan matriks A dan B
A = np.array([[3, 1, 2],
              [2, 1, 1],
              [4, 0, 2]])

B = np.array([[1, 2, 1],
              [3, 1, 1],
              [1, 1, 0]])

# Menghitung determinan matriks A dan B
det_A = np.linalg.det(A)
det_B = np.linalg.det(B)

print(f"Determinan matriks A: {det_A}")
print(f"Determinan matriks B: {det_B}")

# Menghitung invers matriks A dan B jika determinannya tidak nol
if det_A != 0:
    inv_A = np.linalg.inv(A)
    print("Inverse matriks A:")
    print(inv_A)
else:
    print("Matriks A tidak memiliki invers karena determinannya nol.")

if det_B != 0:
    inv_B = np.linalg.inv(B)
    print("Inverse matriks B:")
    print(inv_B)
else:
    print("Matriks B tidak memiliki invers karena determinannya nol.")