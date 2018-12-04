# f = open('tweets_3.json')
import json
import csv

with open('C:\\Users\\bharti\\Desktop\\Social_Media_Mining\\Notebooks\\final paper\\tweets_3.json') as file:
    data = json.load(file)

with open("data.csv", "w") as file:
    csv_file = csv.writer(file)
    for item in data:
        csv_file.writerow([item['pk'], item['model']] + item['fields'].values())
