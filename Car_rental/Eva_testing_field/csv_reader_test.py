import csv

with open ("Eva_testing_field/customer.csv", "r", encoding = "utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    match1_value = 1
    match2_value = 1
    customer_id_filter = input("Customer ID: ")
    age_filter = input("Age: ")
    for line in csv_reader:
        
        if line["Customer ID"] == customer_id_filter or line["Age"] == age_filter:
            print(line["Name"], "\t", line["Age"], "\t", line["Phone"])
            if line["Customer ID"] == customer_id_filter:
                match1_value += 1
            if line["Age"] == age_filter:
                match2_value += 1
        
    if match1_value == 1 and customer_id_filter != "":
        print(customer_id_filter, "was not found")
    
    if match2_value == 1 and age_filter != "":
        print("No customers are", age_filter, "years old.")
        
        

# with open ("Eva_testing_field/customer.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file)

#     for line in csv_reader:
#         print("\t".join(line))
