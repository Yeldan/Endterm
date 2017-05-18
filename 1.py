import collections
import requests
from bs4 import BeautifulSoup
import urllib
from urllib.parse import *
start_url = "https://yvision.kz"

counters = []
def reader(text):
	from collections import Counter
	wordcount = Counter(text.replace(',','').split())
	remove = ['by', 'to', 'through', 'a', 'an', 'and', 'the', 'as', 'at', 'but', 'for', 'into', 'of', 'off', 'up', 'with', 'via', 'than', 'on', 'but']
	for word in remove:
		if word in wordcount:
			del wordcount[word]
	print(wordcount)

def parse_url(url):
	r = requests.get(url)
	html = r.text
	soup = BeautifulSoup(html, "html.parser")
	text = soup.select("body")[0].text
	base_url = url
	#page_counter = count_words(text)
	#global counters
	#counters.append(page_counter)
	links = soup.select('a')
	for link in links:
		if link.has_attr('href'):
			href = link["href"]
			#соединяем URL если он не был абсолютным 
			new_url = urljoin(base_url, href, allow_fragments = False)
			new_url = urldefrag(new_url).url
			r = requests.get(new_url)
			html = r.text
			soup = BeautifulSoup(html, "html.parser")
			text = soup.select("body")[0].text
			lines = (line.strip() for line in text.splitlines())
			chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
			text = '\n'.join(chunk for chunk in chunks if chunk)
			d = reader(text)
			print(d)


parse_url(start_url)	
