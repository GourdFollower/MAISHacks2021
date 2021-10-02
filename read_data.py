import csv

with open("mushrooms.csv") as mush:
    csv_reader = csv.reader(mush, delimiter=",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\tThis mushroom is {row[0]}')
            line_count += 1
    print(f'Processed {line_count} lines.')