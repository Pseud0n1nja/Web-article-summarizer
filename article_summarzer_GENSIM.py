from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
 
 

from bs4 import BeautifulSoup
from urllib.request import urlopen
# 
def get_only_text(url):
 """ 
  return the title and the text of the article
  at the specified url
 """
 page = urlopen(url)
 soup = BeautifulSoup(page, "lxml")
 text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
 return soup.title.text, text    
 
 
url="https://www.wired.co.uk/article/electric-car-sales-china-vs-tesla"
text = get_only_text(url)
 
print ('Summary:')   
print (summarize(str(text), ratio=0.1))
 
print ('\nKeywords:')
 
# higher ratio => more keywords
print (keywords(str(text), ratio=0.05))
