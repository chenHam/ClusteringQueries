import powerSetFinder as psf;
import csv;

columns = ['name', 'year', 'grapes', 'country', 'region', 'description', 'picture']

powerset = psf.listToPowerset(columns)
arr = []

for (cols) in powerset:
    arr.append(', '.join(cols))

with open('queries.csv', 'w', newline='') as csvfile:
    fieldnames = ['select', 'columns', 'from', 'table']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for (str) in arr:
        writer.writerow({'select': 'select', 'columns': str, 'from': 'from', 'table': 'wines'})
