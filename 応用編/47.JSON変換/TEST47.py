#47.JSON変換
#オブジェクトからJSOM文字列
import json

json_data={'Python':'Python-izm.com','SerchEngine':('google.co.jp','yahoo.co.jp')}

print(type(json_data))
encode_json_data=json.dumps(json_data)

print(encode_json_data)
print(type(encode_json_data))

print('=================================')

#見やすい形で変換
import json

json_data2={'Python':'Python-izm.com','SerchEngine':('google.co.jp','yahoo.co.jp')}

encode_json_data2=json.dumps(json_data2,indent=4)

print(encode_json_data2)

print('=================================')

#JSON文字列からオブジェクト
import json

json_data3={'Python':'Python-izm.com','SerchEngine':('google.co.jp','yahoo.co.jp')}

encode_json_data3=json.dumps(json_data3)

print(type(encode_json_data3))
decode_json_data3=json.loads(encode_json_data3)

print(decode_json_data3)
print(type(decode_json_data3))

