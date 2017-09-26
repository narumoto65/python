#coding:utf-8
from sklearn import tree
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import csv

x1 = [0] * 1048
x2 = [0] * 1048
x3 = [0] * 1048
x4 = [0] * 1048
def henkan():
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

def prep():
    inpu_t = ['maruyamasan2.csv','okudasan2.csv','kawanosan2.csv','fukuisan2.csv','mimatasan2.csv','wakamatsusan2.csv']
    output = ['text1.csv','text2.csv','text3.csv','text4.csv','text5.csv','text7.csv']
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
def yomikomi():
    inpu_t = ['text1.csv','text2.csv','text3.csv','text4.csv','text5.csv','text7.csv']
    for i in range(len(inpu_t)):
        f = open(inpu_t[0])
        data = f.read()
        print "data:" + str(i + 1)
        print data
        f.close()

def group1():
    inpu_t = ['text1.csv','text2.csv','text3.csv','text4.csv','text5.csv','text7.csv']
    out = ['group1.csv','group2.csv','group3.csv']
    f=open(inpu_t[0],'rb')
    g=open(inpu_t[1],'rb')
    dataReader = csv.reader(f)
    dataReader2 = csv.reader(g)
    for row in dataReader:
        i = 0
        chars = list(row)
        # if chars[0].isdigit:
        #     print int(chars[0])
        for j in range(len(row)-1):
            if chars[j].isdigit:
                #print(int(chars[j]))
                x1[i] += int(chars[j])
                i += 1
    print i
    for row2 in dataReader2:
        d = 0
        chars2 = list(row2)
        for k in range(len(row2)-1):
            if chars2[k].isdigit:
                x1[d] += int(chars2[k])
                d += 1
    print x1    

    f=open(inpu_t[2],'rb')
    g=open(inpu_t[3],'rb')
    dataReader = csv.reader(f)
    dataReader2 = csv.reader(g)
    for row in dataReader:
        i = 0
        chars = list(row)
        # if chars[0].isdigit:
        #     print int(chars[0])
        for j in range(len(row)-1):
            if chars[j].isdigit:
                #print(int(chars[j]))
                x2[i] += int(chars[j])
                i += 1
    # print i
    for row2 in dataReader2:
        d = 0
        chars2 = list(row2)
        for k in range(len(row2)-1):
            if chars2[k].isdigit:
                x2[d] += int(chars2[k])
                d += 1
    print x2 

    f=open(inpu_t[4],'rb')
    g=open(inpu_t[5],'rb')
    dataReader = csv.reader(f)
    dataReader2 = csv.reader(g)
    for row in dataReader:
        i = 0
        chars = list(row)
        # if chars[0].isdigit:
        #     print int(chars[0])
        for j in range(1047):
            if chars[j].isdigit:
                #print(int(chars[j]))
                x3[i] += int(chars[j])
                i += 1
    print i
    for row2 in dataReader2:
        d = 0
        chars2 = list(row2)
        for k in range(1047):
            if chars2[k].isdigit:
                x3[d] += int(chars2[k])
                d += 1
    print x3 

    f=open(inpu_t[2],'rb')
    g=open(inpu_t[3],'rb')
    dataReader = csv.reader(f)
    dataReader2 = csv.reader(g)
    for row in dataReader:
        i = 0
        chars = list(row)
        # if chars[0].isdigit:
        #     print int(chars[0])
        for j in range(1047):
            if chars[j].isdigit:
                #print(int(chars[j]))
                x4[i] += int(chars[j])
                i += 1
    print i
    for row2 in dataReader2:
        d = 0
        chars2 = list(row2)
        for k in range(1047):
            if chars2[k].isdigit:
                x4[d] += int(chars2[k])
                d += 1
    print x4 

#yomikomi()
group1()
#prep()
#henkan()
    
#まだ個人のデータを読み込んだだけ
# これにチームメンバーのデータを全て足す
# チーム毎にパフォーマンスレベルをラベルする
xa = [x1,x2,x3]
y = ['advanced','intermediate','beginner']
clf = tree.DecisionTreeClassifier()
clf = SVC()
test_x = [x4]
test_y = ['advanced']
clf = clf.fit(xa,y)
prediction = clf.predict(test_x)
print prediction
#print(accuracy_score(test_y,prediction))
