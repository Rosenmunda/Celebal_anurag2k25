n = 5  

# Lower Triangular
print("Lower Triangular:")
for i in range(1, n + 1):
    print("* " * i)

# Upper Triangular
print("\nUpper Triangular:")
for i in range(n, 0, -1):
    print("  " * (n - i) + "* " * i)

# Pyramid
print("\nPyramid:")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
