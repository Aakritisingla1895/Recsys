from Bio import Entrez
from Bio import Medline
from tqdm import tqdm
import pandas

import csv

from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd



# Change this email to your email address
Entrez.email = "aakritisingla18@gmail.com"

keyword = "artificial intelligence"

result = Entrez.read(Entrez.esearch(db="pubmed", retmax=10, term=keyword))
print(
    "Total number of publications that contain the term {}: {}".format(
        keyword, result["Count"]
    )
)

# Fetch all ids
MAX_COUNT = result["Count"]
result = Entrez.read(
    Entrez.esearch(db="pubmed", retmax=result["Count"], term=keyword)
)

ids = result["IdList"]

batch_size = 100
batches = [ids[x: x + 100] for x in range(0, len(ids), batch_size)]

record_list = []
for batch in tqdm(batches):
    h = Entrez.efetch(db="pubmed", id=batch, rettype="medline", retmode="text")
    records = Medline.parse(h)
    record_list.extend(list(records))
print("Complete.")



with open("ai_network_output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(record_list)