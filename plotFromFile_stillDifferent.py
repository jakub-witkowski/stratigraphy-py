import csv
with open('1050.csv') as f:
    reader = csv.reader(f)
    columns_as_lists = [list(c) for c in zip(*reader)]
print(columns_as_lists[0])  # All the values in the first column of your CSV
print(columns_as_lists[1])  # All the values in the second column of your CSV