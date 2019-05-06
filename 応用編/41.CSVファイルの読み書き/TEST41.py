#41.CSVファイルの読み書き
#csvファイルの書き込み
import csv
csv_file=open('./python.csv','w',newline='')
writer=csv.writer(csv_file)

row=('python','-','izm','1')
writer.writerow(row)

rows=[]
rows.append(('python','-','izm','2'))
rows.append(('python','-','izm','2'))
rows.append(('p,y,t,h,o,n','-','i,z,m','4'))

writer.writerows(rows)

csv_file.close()

print('==============================')
#フォーマット指定
import csv
csv_file2=open('./python_2.csv','w',newline='')
writer2=csv.writer(
    csv_file2,
    quoting=csv.QUOTE_ALL,
    delimiter=':',
    quotechar='`'
    )

row2=('python','-','izm','1')
writer2.writerow(row2)

rows2=[]
rows2.append(('python','-','izm','2'))
rows2.append(('python','-','izm','2'))
rows2.append(('p,y,t,h,o,n','-','i,z,m','4'))

writer2.writerows(rows2)

csv_file2.close()

print('==============================')

#あらかじめ用意されているCSVフォーマット
import csv
csv_file3=open('./python_3.csv','w',newline='')
writer3=csv.writer(
    csv_file3,
    dialect=csv.excel_tab
    )

row3=('python','-','izm','1')
writer3.writerow(row3)

rows3=[]
rows3.append(('python','-','izm','2'))
rows3.append(('python','-','izm','2'))
rows3.append(('p,y,t,h,o,n','-','i,z,m','4'))

writer3.writerows(rows3)

csv_file3.close()

print('==============================')

#独自のフォーマットを定義する
import csv

class CustomFormat(csv.excel):
    quoting = csv.QUOTE_ALL

csv_file4=open('./python_4.csv','w',newline='')
writer4=csv.writer(
    csv_file4,
    dialect=CustomFormat
    )

row4=('python','-','izm','1')
writer4.writerow(row4)

rows4=[]
rows4.append(('python','-','izm','2'))
rows4.append(('python','-','izm','2'))
rows4.append(('p,y,t,h,o,n','-','i,z,m','4'))

writer4.writerows(rows4)

csv_file4.close()

print('==============================')

#独自のフォーマットを登録する
import csv

class CustomFormat5(csv.excel):
    quoting = csv.QUOTE_ALL

#登録しておく
csv.register_dialect('myformat',CustomFormat5)

csv_file5=open('./python_5.csv','w',newline='')
writer5=csv.writer(
    csv_file5,
    dialect='myformat'
    )

row5=('python','-','izm','1')
writer5.writerow(row5)

rows5=[]
rows5.append(('python','-','izm','2'))
rows5.append(('python','-','izm','2'))
rows5.append(('p,y,t,h,o,n','-','i,z,m','4'))

writer5.writerows(rows5)

csv_file5.close()

print('==============================')

#csvファイルの読み込み
import csv

csv_file6 = open('./python_6.csv','r',newline='')
reader=csv.reader(csv_file6)

for row in reader:
    print('---------------------')
    for cell in row:
        print(cell)

csv_file6.close()