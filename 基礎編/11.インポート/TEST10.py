import TestMod
test_class_1 = TestMod.TestClass()
test_class_1.TestMethod('1')


#途中からインポートする場合は「from」を使う
from TestMod import TestClass

test_class_2= TestClass()
test_class_2.TestMethod('2')

#別名インポート
from datetime import datetime
print(datetime.today())

from datetime import datetime as d
print(d.today())