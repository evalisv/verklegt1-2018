import csv

with open ("Eva_testing_field/customer.csv", "r", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        newline = " ".join(line)
        print(newline)