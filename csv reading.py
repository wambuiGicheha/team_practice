import csv
#opening the olympic file with csv reader
with open("results.csv", encoding='utf-8') as f:
    reader = csv.reader(f)
    for _ in range(6):
        print(next(reader))
        