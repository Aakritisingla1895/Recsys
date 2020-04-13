import pandas as pd
from sqlalchemy import create_engine

# read CSV file
column_names = ['author_name','affliations', 'article_title', 'doi', 'volume']



df = pd.read_csv('E:/Dissertation/Project/RecomenSys/ai_test.csv', header = None, names = column_names)

print(df)

df = pd.read_csv('E:/Dissertation/Project/RecomenSys/prep_ai_dataset.csv', header = 0)

print(df)


