import scholarly
import csv

# Retrieve the author's data, fill-in, and print

search_query = scholarly.search_author('Steven A Cholewiak')
author = next(search_query).fill()
print(author)

# Print the titles of the author's publications
print([pub.bib['title'] for pub in author.publications])

# Take a closer look at the first publication
pub = author.publications[0].fill()
print(pub)

# Which papers cited that publication?
#print([citation.bib['title'] for citation in pub.get_citedby()]).encode("utf-8")


csv_file = "Names.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=" ")
        writer.writeheader()
        for data in pub:
            writer.writerow(data)
except IOError:
    print("I/O error")