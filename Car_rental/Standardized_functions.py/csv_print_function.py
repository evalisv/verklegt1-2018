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

        print(line[], "\t", line[])   

# Prenta út allt skjalið eins og það legur sig. 

with open ("","r") as csv_file:
    # Það þarf ekki að nota DictReader nema maður sé að leita að einhverju
    csv_reader = csv.reader(csv_file) 

    for line in csv_reader:
        # .join(line) breytir línunni úr lista yfir í streng
        print("\t".join(line))  




