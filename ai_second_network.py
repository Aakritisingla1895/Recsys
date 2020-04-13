from Bio import Entrez
from Bio import Medline
from tqdm import tqdm
from collections import Counter
import seaborn as sns
import csv
import pandas as pd
import numpy as np
# Change this email to your email address
Entrez.email = "A.N.Other@example.com"

keyword = "machine learning"

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

ai_network = []
ai_dict={}
o=0
filename = 'ai_second_network.csv'
#file=open('ai_second_network.csv','w')
for batch in tqdm(batches):
    h = Entrez.efetch(db="pubmed", id=batch, rettype="medline", retmode="text")
    journals = Medline.parse(h)
    journals_list = ai_network.extend(list(journals))
    #ai_network.append(journals_list)
print(journals_list)

    

    

    
    #df = pd.DataFrame(ai_network, columns = ['Name', 'Age'])  
    #for item in ai_network:
     #   with open("ai_output.csv", "w") as f:
      #      writer = csv.writer(f)
       #     writer.writerows(ai_network)

     

    #for item in ai_network:

      

  
    #for item in ai_network:
     #   
       

    

   
    #file.close()print(df)
print("Complete.")

