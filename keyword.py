from bs4 import BeautifulSoup
import requests
from nltk.tokenize import RegexpTokenizer
import nltk
import pandas as pd 

words_ns = []
flag=0

words=[]
tokens=[]

url=input()
r = requests.get(url)
html=r.text
soup = BeautifulSoup(html, "html5lib")
text = soup.get_text()

tokenizer = RegexpTokenizer('\w+')
tokens = tokenizer.tokenize(text)

for word in tokens:
    words.append(word.lower())
    
sw = nltk.corpus.stopwords.words('english')
    
for word in words:
    if word not in sw:
        words_ns.append(word)
        
df = pd.read_csv("bad-words.csv") 

for keyword in words_ns:
    if keyword in df.values:
        flag=flag+1
        
print(flag)