#coding:utf-8
import csv
inpu_t = ['maruyamasan2.csv','okudasan2.csv','kawanosan2.csv','fukuisan2.csv','mimatasan2.csv','wakamatsusan2.csv']
output = ['text1.csv','text2.csv','text3.csv','text4.csv','text5.csv','text6.csv']
for i in range(6):
    f = open(inpu_t[i],'rb')
    d = open(output[i],'w')
    dataReader=csv.reader(f)
    for row in dataReader:
        chars= list(row)
        for i in range(len(row)):
            if chars[i].isdigit():
                d.write(chars[i])
                d.write(',')
        d.close

print output[1]