import numpy as np
from multiprocessing import Pool

def multiply_row(args):
    row, matrix_b = args
    return np.dot(row, matrix_b)

if __name__ == "__main__":
    A = np.random.rand(500, 300)
    B = np.random.rand(300, 400)

    with Pool() as pool:
        result = pool.map(multiply_row, [(row, B) for row in A])

    result_matrix = np.array(result)
    print("Multiplication complete. Result shape:", result_matrix.shape)
