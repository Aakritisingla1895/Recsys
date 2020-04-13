import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='prep_ai_data')
cursor = mydb.cursor()

csv_data = csv.reader('ai_test.csv')
for row in csv_data:

    cursor.execute('INSERT INTO author(author_name, \
          author_affliations, \ article_title, \ article_doi, \ article_volume)' 
          'VALUES("%s", "%s", "%s", "%s", "%s")', 
          row)
#close the connection to the database.
mydb.commit()
cursor.close()
print ("Done")