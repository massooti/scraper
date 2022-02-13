from bs4 import BeautifulSoup
import pandas as pd
import requests
from unidecode import unidecode
import re

names = []  # List to store name of the product
phones = []  # List to store price of the product
ratings = []  # List to store rating of the product
educations = []
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Content-Type': 'text/html',
}

url = "https://teaching.iranmodares.com/teaching-index.php"
root = requests.get(url, headers=header)


def progressbar(curr, total, full_progbar):
    frac = curr/total
    filled_progbar = round(frac*full_progbar)
    print('\r', '#'*filled_progbar + '-'*(full_progbar -
          filled_progbar), '[{:>7.2%}]'.format(frac), end='')


for i in range(826):
    page = url + str("?page={}".format(i))
    soup = BeautifulSoup(root.content, 'html.parser')
    for div in soup.findAll('div', attrs={'class': 'pic-panel-left'}):
        name = div.find('div', attrs={'class': 'teacher-name'})
        phone = div.find('div', attrs={'class': 'phone'})

        education = div.find('div', attrs={'class': 'teacher-reshte'})
        names.append(name.text)
        phones.append(phone.text)
        educations.append(education.text)
    progressbar(i, 826, 20)


df = pd.DataFrame({'phone': phones, 'name': names,
                   'education': educations, })
df.to_csv('output.csv', index=False, encoding='utf-8',
          header=['phone', 'name', 'education'])
