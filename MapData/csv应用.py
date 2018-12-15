# @Time    : 2018/11/26 21:13
# @Author  : pangguoyi
# @File    : csv应用.py

import csv

#csv 写入
stu1 = ['marry',26]
stu2 = ['bob',23]
#打开文件，追加a
out = open('Stu_csv.csv','a', newline='')  #newline='' 表示每写入一次数据时，与上次数据间隔，不写该表达式，默认是间隔一行
#设定写入模式
csv_write = csv.writer(out,dialect='excel')  #定义格式
#写入具体内容
csv_write.writerow(stu1)
csv_write.writerow(stu2)



title=1
location=2
price = 3
url = 4
with open('house.csv', 'a', encoding='utf-8', newline='') as f1:
    csv_write = csv.writer(f1, dialect='excel')
    csv_write.writerow([title, location, price, url])

