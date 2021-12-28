import requests
from bs4 import BeautifulSoup


url = 'https://invoice.etax.nat.gov.tw/'
html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')
all1 = sp.find("table", class_="etw-table-bgbox etw-tbig")

def show():
    tb = sp.find('span', class_='font-weight-bold etw-color-red')
    print("特別獎:", tb.text)

    t = sp.find_all('span', class_='font-weight-bold etw-color-red')[1]
    print("特獎:", t.text)

    head1 = sp.find("p", class_="etw-tbiggest mb-md-4")
    head2 = sp.find_all("p", class_="etw-tbiggest mb-md-4")[1]
    head3 = sp.find_all("p", class_="etw-tbiggest mb-md-4")[2]
    print("頭獎:", head1.text, end="")
    print(head2.text, end="")
    print(head3.text)

    add1 = sp.find_all("span", class_="font-weight-bold etw-color-red")
    print("增開六獎:", add1[-1].text)

show()