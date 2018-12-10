import csv

with open ("Eva_testing_field/customer.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)


    for line in csv_reader:
        print(line)

