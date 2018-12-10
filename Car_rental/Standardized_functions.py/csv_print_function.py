# Ennþá í vinnslu
# Þetta mun vera einhver syntax errors en það er því það þarf að fylla út það sem vantar.


# Filtered útprentun eftir flokki, t.d til að prenta aðeins út nöfn viðskiptavina. eða nöfn og auðkenni. 
import csv

with open ("", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)   #Til þess að geta filterað út frá lyklum þarf að nota DictReader

    for line in csv_reader:
        # Prentar aðeins út gildin sem eru tengd við þá lykla sem settir eru i hornklofana.
        # Dæmi: print(line["Name"], "\t", line["Email"], "\t", line["Phone"])
        # "\t" er fyrir tabs
        # Format nauðsynlegt, kemur fljótlega.
        print(line[], line[])   

# Prenta út allt skjalið eins og það legur sig. 

with open ("","r") as csv_file:
    # Það þarf ekki að nota DictReader nema maður sé að leita að einhverju
    csv_reader = csv.reader(csv_file) 

    for line in csv_reader:
        # .join(line) breytir línunni úr lista yfir í streng
        print("\t".join(line))  


# Að finna einn hlut eftir lykli
# Dæmi:
with open ("", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Setjið inn það breytu nafn sem passar inn í staðinn fyrir customer_id_filter,
    customer_id_filter = input("")
    match_value = 1
    for line in csv_reader:
        # Setjið inn þann lykil sem á að filtera eftir, "Customer ID" er aðeins hér fyrir dæmið.
        # if setningin ber saman gildið sem er í lyklinum og inputið, ef það er eins þá prentast eitthvað út.
        if line["Customer ID"] == customer_id_filter:
            print(line[""], "\t", line[""], "\t", line[""])
        
    if match_value == 1:
        # Notify that something wasn't found
        print()
            

# Til að filtera eftir 2 eða fleiri gildum, þar sem aðeins eitt gildið þarf að vera satt. T.d. að finna pöntun eftir bókunarnúmeri eða Customer ID
with open ("", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # match_value til þess að geta tilkynnt að eitthvað hafi ekki fundist
    match1_value = 1
    match2_value = 1
    # filter_1 gæti t.d. heitið booking_number_filter og inputið myndi þá vera input("Booking number: ")
    # myndi þá vera:    booking_number_filter = input("Booking number: ")
    filter_1 = input("")
    filter_2 = input("")
    for line in csv_reader:
        
        if line[""] == filter_1 or line[""] == filter_2:
            # Some action
            if line[""] == filter_1:
                match1_value += 1
            if line[""] == filter_2:
                match2_value += 1
    
    if match1_value == 1 and filter_1 != "":
        print(filter_1, "t.d: was not found")
    
    if match2_value == 1 and filter_2 != "":
        print(filter_2, "t.d: was not found")
    
# Dæmi:
#  with open ("", "r") as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     match1_value = 1
#     match2_value = 1
    
#     booking_number_filter = input("Booking number: ")
#     customer_id_filter = input("Customer ID: ")
#     for line in csv_reader:
        
#         if line["Booking Number"] == booking_number_filter or line["Customer ID"] == customer_id_filter:
#             print(line["Name"], "\t", line["Phone"], "\t", line["Email"])
#             if line["Booking Number"] == booking_number_filter:
#                 match1_value += 1
#             if line["Customer ID"] == customer_id_filter:
#                 match2_value += 1
    
#     if match1_value == 1 and booking_number_filter != "":
#         print("No order with", booking_number_filter, "as booking number")
    
#     if match2_value == 1 and customer_id_filter != "":
#         print("No customer with the ID:", customer_id_filter)

