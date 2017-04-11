import urllib2
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

url = 'http://www.metacritic.com/game/pc/yooka-laylee/critic-reviews'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,}
req = urllib2.Request(url, None, headers)

page = urllib2.urlopen(req)

soup = BeautifulSoup(page, "lxml")
title = soup.find_all('h1', class_='product_title')
all_divs=soup.find_all('div', class_='review_body')

dels = ""

for p in title:
	for q in p:
		try:
			dels+=q.string.encode('UTF-8')
		except:
			dels+=""

dels = dels.split()
print dels
string = ""
for p in all_divs:
	try:
		string+=p.string.encode('UTF-8')
	except:
		string+=""

string = string.split()
print string
for rem in dels:
	if str(rem) in string: 
		string.remove(str(rem))
	rem = rem.replace('-', ' ')
	rem = rem.replace('.', ' ')
	rem = rem.replace('_', ' ')
	rem = rem.split()
	for srem in rem:
		print srem
		if str(srem) in string:
			print "Here"
			string.remove(str(srem))

string = " ".join(string)

wordcloud = WordCloud().generate(string)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
