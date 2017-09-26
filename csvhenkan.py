#coding:utf-8
import csv
f = open('hoge.csv','rb')
d = open('text.txt','w')
dataReader=csv.reader(f)
for row in dataReader:
    chars= list(row)
    for i in range(len(row)):
        if chars[i].isdigit():
            d.write(chars[i])
            d.write(',')
    d.close
            #print(chars[i])