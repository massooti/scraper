from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import requests
# from webdriver_manager.chrome import ChromeDriverManager
# browser = webdriver.Chrome()
# driver = webdriver.Chrome(ChromeDriverManager().install())

names=[] #List to store name of the product
phones=[] #List to store price of the product
ratings=[] #List to store rating of the product
education=[]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Content-Type': 'text/html',
}
x = requests.get("https://teaching.iranmodares.com/teaching-index.php")
print(x)
exit()
content = x.text
print(content)
exit()
# soup = BeautifulSoup(content)
# for div in soup.findAll('div',href=True, attrs={'class':'pic-panel-left'}):
# name=a.find('div', attrs={'class':'_3wU53n'})
# price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
# rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
# products.append(name.text)
# prices.append(price.text)
# ratings.append(rating.text) 


df = pd.DataFrame({'name':names,'phone':phones,'education':education,'category':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')