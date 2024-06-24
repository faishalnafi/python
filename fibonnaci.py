import numpy as np

def fibonacci(n):
    fib_sequence = np.zeros(n, dtype=int)
    fib_sequence[0] = 0
    if n > 1:
        fib_sequence[1] = 1
        for i in range(2, n):
            fib_sequence[i] = fib_sequence[i-1] + fib_sequence[i-2]
    return fib_sequence

# Input dari pengguna
n = int(input("Masukkan jumlah bilangan Fibonacci yang ingin dihitung: "))

# Menghitung deret Fibonacci
fib_sequence = fibonacci(n)

# Menampilkan hasil
print(f"Deret Fibonacci sebanyak {n} bilangan: {fib_sequence}")
