def print_pattern(rows):
    for i in range(rows):
        for j in range(i,rows-1):
            print("*", end=" ")
        print()

# Example usage
rows = 6
print_pattern(rows)