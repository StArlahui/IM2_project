rows = int(input("Enter row: "))
cols = int(input("Enter col: "))

matrix = {}

for r in range(rows):
    print(f"\nRow {r+1}")
    for c in range(cols):
        num = float(input(f"Enter number{c+1}: "))
        matrix[(r, c)] = num

print("\nThe numbers are:\n")
for r in range(rows):
    row_data = []
    for c in range(cols):
        row_data.append(str(matrix[(r, c)]))
    print(" ".join(row_data))

search = float(input("\nSearch: "))

for key, value in matrix.items():
    if value == search:
        print(f"Number {search} found at Row {key[0]}, Col {key[1]}")