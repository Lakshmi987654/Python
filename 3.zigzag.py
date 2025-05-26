def zigzag_pattern(n):
    for i in range(n):
        # Print spaces to create zigzag indentation
        if i % 2 == 0:
            print(" " * 0 + "*" * n)
        else:
            print(" " * (n//2) + "*" * n)

zigzag_pattern(5)
