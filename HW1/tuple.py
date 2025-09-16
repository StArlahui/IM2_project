rows = int(input("Enter row: "))
cols = int(input("Enter col: "))

matrix = []

for r in range(rows):
    row_data = []
    print(f"\nRow {r+1}")
    for c in range(cols):
        num = float(input(f"Enter number{c+1}: "))
        row_data.append(num)
    matrix.append(tuple(row_data))   
matrix = tuple(matrix)   

print("\nThe numbers are:\n")
for row in matrix:
    print(" ".join(map(str, row)))

search = float(input("\nSearch: "))

for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == search:
            print(f"Number {search} found at Row {r}, Col {c}")