# Magic-square-finder
This Python script generates, displays, and visualizes odd-sized magic squares using the Siamese (De la Loubère) method. A magic square is a grid of numbers where the sums of values in each row, column, and diagonal are equal (the magic constant).
Key Components:
Generate Magic Square (generate_magic_square(n)):
![Magic-number0find](https://github.com/user-attachments/assets/47a1ff38-7307-462d-8b19-e928e7735154)

Uses the Siamese method to construct an n x n magic square for odd n.

Starts at the top-middle cell and moves diagonally upward-right. If a cell is occupied, it moves downward instead.

Wraps around grid edges using modulo arithmetic.

Text-Based Display (print_magic_square(square)):

Prints the magic square with formatted alignment for readability.

Heatmap Visualization (plot_magic_square(square)):

Uses matplotlib to create a color-coded grid with superimposed numbers.

The colormap (viridis) highlights value distributions, and a colorbar provides a reference.

Interactive Loop:

Prompts the user for an odd integer size (or 0 to exit).

Validates inputs, displays the magic square, calculates the magic constant (n*(n²+1)//2), and renders the plot.

Gracefully handles invalid inputs (non-integers or even numbers).

Features:
Educational Tool: Demonstrates the construction of magic squares algorithmically.

Visual Appeal: Combines numerical output with a graphical heatmap for intuitive understanding.

User-Friendly: Includes input validation and clear error messages.

Usage Example:
python
Copy
# Enter "3" when prompted to generate a 3x3 magic square:
#   8   1   6
#   3   5   7
#   4   9   2
# Magic Constant: 15
Dependencies: Requires numpy for array operations and matplotlib for plotting. Ideal for math enthusiasts or educators teaching combinatorial algorithms.
