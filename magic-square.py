import numpy as np
import matplotlib.pyplot as plt

def generate_magic_square(n):
    if n % 2 == 0:
        raise ValueError("This method works only for odd-sized magic squares.")

    magic_square = np.zeros((n, n), dtype=int)
    row, col = 0, n // 2

    for num in range(1, n**2 + 1):
        magic_square[row, col] = num
        new_row, new_col = (row - 1) % n, (col + 1) % n

        if magic_square[new_row, new_col] != 0:
            row = (row + 1) % n
        else:
            row, col = new_row, new_col

    return magic_square

def print_magic_square(square):
    for row in square:
        print(" ".join(f"{num:3d}" for num in row))

def plot_magic_square(square):
    fig, ax = plt.subplots(figsize=(10, 10))
    im = ax.imshow(square, cmap='viridis')

    for i in range(square.shape[0]):
        for j in range(square.shape[1]):
            text = ax.text(j, i, square[i, j], ha="center", va="center", color="w")

    plt.colorbar(im)
    plt.title(f"Magic Square of order {square.shape[0]}")
    plt.show()

# Interactive part
while True:
    try:
        n = int(input("Enter the size of the magic square (odd number, or 0 to exit): "))
        if n == 0:
            break
        if n % 2 == 0:
            print("Please enter an odd number.")
            continue

        magic_square = generate_magic_square(n)

        print("\nMagic Square:")
        print_magic_square(magic_square)

        print(f"\nMagic Constant: {n * (n**2 + 1) // 2}")

        plot_magic_square(magic_square)

    except ValueError as e:
        print(f"Error: {e}")

print("Program ended. Thank you!")
