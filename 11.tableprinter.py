def print_table(data):
    # Calculate max width of each column
    cols = len(data[0])
    col_widths = [0] * cols
    for row in data:
        for i in range(cols):
            col_widths[i] = max(col_widths[i], len(str(row[i])))

    # Print each row with padding
    for row in data:
        row_str = ""
        for i in range(cols):
            cell = str(row[i])
            # Left align each cell within its column width + 2 spaces padding
            row_str += cell.ljust(col_widths[i] + 2)
        print(row_str)

# Example usage:
table = [
    ["Name", "Age", "Occupation"],
    ["Alice", "30", "Engineer"],
    ["Bob", "24", "Designer"],
    ["Charlie", "29", "Teacher"]
]

print_table(table)
