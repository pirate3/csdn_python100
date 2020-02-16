d = {'a': 123, 'b': '456', 'c': 'xyz'}
print(d)
print(type(d))

import json

# 对象转json
json_str = json.dumps(d)
print(json_str)
print(type(json_str))  # <class 'str'>

# json转对象
d1 = json.loads(json_str)
print(d1)
print(type(d1))  # <class 'dict'>
