#print
#基本的な使い方(python3)
print('python')
print('-')
print('izm')
print('com')

#基本的な使い方(python2)
#print 'python'
#print '-'
#print 'izm'
#print 'com'

#改行せずに出力(python3)
print('python',end='')
print('-',end='')
print('izm',end='')
print('com')

#改行せずに出力(python2)
#print 'python',
#print '-',
#print 'izm',
#print 'com'

#出力先の変更(python3)
f_obj=open('test.txt','w')
print('python-izm.com',file=f_obj)

#出力先の変更(python2)
#f_obj=open('test.txt','w')
#print >> file=f_obj 'python-izm.com'

#フォーマット出力
print('Python学習サイト:%s' % 'python-izm.com')
print('Python学習サイト:%s-%s.%s' % ('python','izm','com'))

test_int=100+200
test_str='python-izm.cm'
print('サイト開設:%d　日目! %s' % (test_int,test_str) )

#フォーマット出力2
print('Python学習サイト:{}'.format('python-izm.com'))
print('Python学習サイト:{0}-{1}.{2}'.format('python','izm','com'))

test_int=100+200
test_str='python-izm.cm'
print('サイト開設:{1}　日目! {0}'.format(test_str,test_int) )
