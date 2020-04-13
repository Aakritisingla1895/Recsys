from Bio import Entrez
from Bio import Medline
from tqdm import tqdm
import pandas as pd
import json
import csv
from collections import Counter
import seaborn as sns
import ast
import matplotlib.pyplot as plt

# Change this email to your email address
Entrez.email = "A.N.Other@example.com"

keyword = "Cancer disease biology"

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
    #print (record_list)
print("Complete.")  

publication_data = pd.DataFrame(record_list)
publication_data.dropna(subset=['TI'], inplace=True)
publication_data["Year"] = (
    publication_data["TI"].astype(str)

)

print(publication_data)


# Converting set to dictionary 
res = dict.fromkeys(publication_data, ) 
print ("final list", res)

# Publications over Time
plt.subplot(2, 2, 2)
yearly = pd.DataFrame(publication_data["Year"].value_counts().reset_index())
yearly.columns = ["Year", "Count"]
sns.lineplot(x="Year", y="Count", data=yearly)
plt.title("Publications over Time")
plt.xlim([1986, 2020])

plt.show()
