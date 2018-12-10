import csv

with open ("Eva_testing_field/customer.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    match_value = 1
    customer_id_filter = input("Customer ID: ")
    for line in csv_reader:
        
        if line["Customer ID"] == customer_id_filter:
            print(line["Name"], "\t", line["Email"], "\t", line["Phone"])
            match_value += 1
        
    if match_value == 1:
        print(customer_id_filter, "was not found")
        
        

# with open ("Eva_testing_field/customer.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file)

#     for line in csv_reader:
#         print("\t".join(line))
