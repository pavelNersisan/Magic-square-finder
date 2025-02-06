import numpy as np
import matplotlib.pyplot as plt
from math import ceil

def generate_magic_square(n):
    """Generate magic squares of any size with optimal algorithms for each type"""
    if n < 1:
        raise ValueError("Size must be ≥ 1")
    
    # Initialize square with zeros
    square = np.zeros((n, n), dtype=np.int64)
    
    # Case 1: Odd order (Siamese method)
    if n % 2 == 1:
        i, j = 0, n//2
        for num in range(1, n*n + 1):
            square[i, j] = num
            ni, nj = (i-1) % n, (j+1) % n
            if square[ni, nj]:
                i = (i+1) % n
            else:
                i, j = ni, nj
    
    # Case 2: Doubly even order (4k)
    elif n % 4 == 0:
        # Create pattern for complement substitution
        pattern = np.array([[1 if (i%4 == j%4) or (i%4 + j%4 == 3) else 0 
                           for j in range(n)] for i in range(n)])
        numbers = np.arange(1, n*n+1).reshape(n, n)
        square = np.where(pattern, numbers, n*n + 1 - numbers)
    
    # Case 3: Singly even order (4k+2 - Strachey method)
    else:
        q = n // 2
        sub = generate_magic_square(q)
        quadrants = [sub, sub + 3*q*q, 
                    sub + 2*q*q, sub + q*q]
        
        # Assemble quadrants
        square[:q, :q] = quadrants[0]
        square[:q, q:] = quadrants[1]
        square[q:, :q] = quadrants[2]
        square[q:, q:] = quadrants[3]
        
        # Adjustments for magic property
        k = (q-1) // 2
        # Swap columns in first rows
        for col in range(k):
            square[[0, q], col] = square[[q, 0], col]
        # Swap middle columns in right half
        for col in range(q + k + 1, n):
            square[:q, col] = square[[q, 0], col - q]
    
    return square

def magic_constant(n):
    """Calculate and explain the magic constant formula"""
    const = n * (n**2 + 1) // 2
    explanation = (f"Magic Constant = n(n² + 1)/2\n"
                  f"               = {n}({n}² + 1)/2\n"
                  f"               = {n}({n**2 + 1})/2\n"
                  f"               = {const}")
    return const, explanation

def plot_magic_square(square, max_display=15):
    """Visualize with magic constant annotation"""
    n = square.shape[0]
    const, explanation = magic_constant(n)
    
    plt.figure(figsize=(10, 10))
    plt.imshow(square, cmap='viridis', interpolation='nearest')
    
    # Add numbers for small squares
    if n <= max_display:
        for i in range(n):
            for j in range(n):
                plt.text(j, i, str(square[i,j]),
                        ha='center', va='center',
                        color='white', fontsize=8)
                
    # Add magic constant explanation
    plt.title(f"Magic Square of Order {n}\n{explanation}", pad=20)
    plt.colorbar(label='Value')
    plt.axis('off')
    
    # Performance note for large squares
    if n > 30:
        plt.text(0.5, 0.95, f"Display simplified for {n}x{n} square",
                ha='center', transform=plt.gca().transAxes,
                bbox=dict(facecolor='white', alpha=0.8))
    
    plt.show()

def benchmark_performance():
    """Performance test for large squares"""
    sizes = [10, 100, 1000]
    print("\nPerformance Benchmark:")
    for s in sizes:
        start = time.time()
        generate_magic_square(s)
        elapsed = time.time() - start
        print(f"Generated {s}x{s} in {elapsed:.4f} seconds")

# Interactive interface remains similar but with performance optimizations
# ... (Previous interface code with input validation)

if __name__ == "__main__":
    import time
    # benchmark_performance()  # Uncomment to test performance
    main()
