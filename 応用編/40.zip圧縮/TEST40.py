#40.zip圧縮
#zipfile
import zipfile

zipFile = zipfile.ZipFile('./compress_1.zip', 'w', zipfile.ZIP_STORED)
zipFile.write('./python.py')
zipFile.write('./python.txt')
zipFile.write('./python.csv')
zipFile.close()

zipFile = zipfile.ZipFile('./commress_2.zip','w',zipfile.ZIP_DEFLATED)
zipFile.write('./python.py')
zipFile.write('./python.txt')
zipFile.write('./python.csv')
zipFile.close()

