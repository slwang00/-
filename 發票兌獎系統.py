# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 10:42:18 2021

@author: slwang
"""

import csv
import requests
from bs4 import BeautifulSoup
#發票號碼的儲存
def push():
    fn = '發票號碼.csv'
    number =[]
    data=''
    while(1):
        data = input('請輸入發票號碼(輸入空白鍵即可停止輸入) :')
        if(len(data)==8 or len(data)==3):
            number.append(data)
        elif data==' ':
            break
        else:
            print('請重新輸入')
    with open(fn,'a',newline=('')) as csvfile:
        write = csv.writer(csvfile)
        for i in number:
            write.writerow([i])
        
#把發票號碼從資料庫裡取出並回傳
def pop():
    fn = '發票號碼.csv'
    number_list=[]
    with open(fn,'r',newline=('')) as csvfile:
        read = csv.reader(csvfile)
        for i in read:
            number_list.append(i[0])
        return number_list

#爬下中獎號碼
def show():
    url = 'https://invoice.etax.nat.gov.tw/'
    html = requests.get(url)
    sp = BeautifulSoup(html.text, 'html.parser')
    all1 = sp.find("table", class_="etw-table-bgbox etw-tbig")
    tb = sp.find('span', class_='font-weight-bold etw-color-red')
    # print("特別獎:", tb.text)

    t = sp.find_all('span', class_='font-weight-bold etw-color-red')[1]
    # print("特獎:", t.text)

    head1 = sp.find("p", class_="etw-tbiggest mb-md-4")
    head2 = sp.find_all("p", class_="etw-tbiggest mb-md-4")[1]
    head3 = sp.find_all("p", class_="etw-tbiggest mb-md-4")[2]
    # print("頭獎:", head1.text, end="")
    # print(head2.text, end="")
    # print(head3.text)

    add1 = sp.find_all("span", class_="font-weight-bold etw-color-red")
    # print("增開六獎:", add1[-1].text)
    win_num_list = [tb.text,t.text,head1.text[1:],head2.text[1:],head3.text[1:],add1[-1].text]
    return win_num_list
    
#比對中獎號碼
def redeem(num="",special1="",special2="",win1="",win2="",win3="",addsix=""):
    if num==special1 :
        return "中了特別獎"
    elif num==special2 :
        return "中了特獎"
    elif len(num)==3 and num==addsix:
        return "中了增開六獎"
    elif num==win1 or num==win2 or num==win3:
        return "中了頭獎"
    elif num[1:]==win1[1:] or num[1:]==win2[1:] or num[1:]==win3[1:]:
        return "中了二獎"
    elif num[2:]==win1[2:] or num[2:]==win2[2:] or num[2:]==win3[2:]:
        return "中了三獎"
    elif num[3:]==win1[3:] or num[3:]==win2[3:] or num[3:]==win3[3:]:
        return "中了四獎"
    elif num[4:]==win1[4:] or num[4:]==win2[4:] or num[4:]==win3[4:]:
        return "中了五獎"
    elif num[5:]==win1[5:] or num[5:]==win2[5:] or num[5:]==win3[5:]:
        return "中了六獎"
    else:
        return "沒中"     
    
#MAIN
print('/===========歡迎使用 發票兌獎系統=============/\n')
while(1):
    key = str(input('/===========請依照功能表遠則功能===========/\n\
                1 ===> 輸入自己擁有的發票號碼\n\
                2 ===> 自動兌獎\n\
                q ===> 結束\n\
                您選擇之功能為：'))
    if key!='1' and key!='2' and key!='q':
        print('請依照功能表遠則功能')
        continue
    elif key=='1':
        push()
    elif key=='2':
        win_num_list = show()
        num_list = pop()
        print('\n\n以下為您的發票中獎結果')
        for i in num_list[0:-1]:
            print('您在發票號碼：',i,redeem(i,win_num_list[0],win_num_list[1],win_num_list[2],win_num_list[3],win_num_list[4],win_num_list[5]))
    elif key == 'q':
        break
    key2 =input('請問是否繼續使用本系統(Y/N)') 
    if key2=='N' or key2=='n':
        break

        