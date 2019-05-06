#26.順序保持ディクショナリ (2.7 - 3.6)
#collections.OrderedDict

#通常
test_dict={}

test_dict['word']='doc'
test_dict['excel']='xls'
test_dict['access']='mdb'
test_dict['powerpoint']='ppt'
test_dict['notepad']='txt'
test_dict['python']='py'

for key in test_dict:
    print(key)

print('======================================')
#collections.OrderedDict版
import collections
test_dict2=collections.OrderedDict()

test_dict2['word']='doc'
test_dict2['excel']='xls'
test_dict2['access']='mdb'
test_dict2['powerpoint']='ppt'
test_dict2['notepad']='txt'
test_dict2['python']='py'

for key in test_dict:
    print(key)