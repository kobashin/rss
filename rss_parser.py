import feedparser
import pandas as pd
from funcs import *

# rss entries
d = feedparser.parse('https://rss.itmedia.co.jp/rss/2.0/mn_carele.xml')

# latest date file
latestDateFile = open('latestDate.txt', 'r', newline='')
latestDate = latestDateFile.read()
latestDateFile.close()

# news database
columns = ['DateTime', 'Title', 'URL']
df = pd.read_csv('news_database.csv', encoding='shift-jis', header=None, names=columns)

addNews = pd.DataFrame(columns=columns)

for entry in d.entries:
    if reshapeDate(entry.published) > reshapeDate(latestDate):
        news = pd.DataFrame([[entry.published, entry.title, entry.link]], columns=columns)
        addNews = pd.concat([addNews, news], axis=0)

df = pd.concat([addNews, df], ignore_index=True)
df.to_csv('news_database.csv', index=False, encoding='shift-jis', header=None)

latestDateFile = open('latestDate.txt', 'w', newline='')
latestDateFile.write(addNews.iloc[0, 0])
latestDateFile.close()
