import pandas as pd

data = pd.read_csv('ai_test.csv')

#print (data)

col_names = data.columns
#print(col_names)


list_of_dict = []
for i in range(data.shape[0]):
    dict= {}
    for name in col_names:
        dict[name]=data.loc[i,name]
    list_of_dict.append(dict)
print (list_of_dict)