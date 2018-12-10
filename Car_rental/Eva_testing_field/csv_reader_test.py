import csv

# with open ("Eva_testing_field/customer.csv", "r") as csv_file:
#     csv_reader = csv.DictReader(csv_file)


#     for line in csv_reader:
#         print(line["Name"], "\t", line["Email"], "\t", line["Phone"])

with open ("Eva_testing_field/customer.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print("\t".join(line))
