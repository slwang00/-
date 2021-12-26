# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 10:42:18 2021

@author: slwang
"""

import csv

def push():
    fn = '發票號碼.csv'
    number =[]
    data=''
    while(data!=' '):
        data = input('請輸入發票號碼 :')
        if(len(data)<8):
            
            number.append(data)
        else:
            print('請重新輸入')
    with open(fn,'w',newline=('')) as csvfile:
        write = csv.writer(csvfile)
        for i in number:
            write.writerow([i])
        
def pop():
    fn = '發票號碼.csv'
    number_list=[]
    with open(fn,'r',newline=('')) as csvfile:
        read = csv.reader(csvfile)
        for i in read:
            number_list.append(i)
        return number_list
# push()