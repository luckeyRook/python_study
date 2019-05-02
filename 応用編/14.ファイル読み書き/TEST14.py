#14.ファイル読み書き

#ファイルの読み込み
f = open('read.txt','r')
for row in f:
    print(row)
f.close()

#ファイルの書き込み
f = open('write.txt','w')
f.write("Pythonで書き込みをしました")
f.close()

#文字コードの指定
fin_sjis = open('read.txt','r',encoding='Shift_jis')
fout_euc = open('euc-jp.txt','w',encoding='euc_jp')
fout_utf = open('utf-8.txt','w',encoding='utf-8')

for row in fin_sjis:
    fout_euc.write(row)
    fout_utf.write(row)

fin_sjis.close()
fout_euc.close()
fout_utf.close()