import csv
d={}
for row in csv.reader(open('final_ai_dataset.dat')):
    d['ID %s' % row[0]] = {'name': row[1], 'affliations': row[2], 'article_title': row[3]}
print (d)
print
user_id = 125
print ('ID %s:') % user_id, d['ID %s' % user_id]
print
print ('ID %s') % user_id
print ('Name:'), d['ID %s' % user_id]['name'],
print ('affliations:'), d['ID %s' % user_id]['affliations'],
print ('article_title:'), d['ID %s' % user_id]['article_title']