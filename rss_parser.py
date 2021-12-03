import feedparser
import csv

d = feedparser.parse('https://rss.itmedia.co.jp/rss/2.0/mn_carele.xml')

output_file = open('news_database.csv', 'a', newline='')
output_writer = csv.writer(output_file)

for entry in d.entries:
    output_writer.writerow([entry.published, entry.title, entry.link])

output_file.close()
