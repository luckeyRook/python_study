#38.環境変数の取得
#os.environ
import os
for env in os.environ:
    print(env)
print('-----------------------------')
print(os.environ.get('windir'))