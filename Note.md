# 补充知识
使用Python的requests库作接口测试——响应结果处理

在实际工作中，很多接口的响应都是json格式的数据，在测试中需要对其进行处理和分析。

设计到json数据处理的方法有两种：序列化和反序列化

python中序列化，简单讲就是将python的字典转换成json格式字符串，以便进行储存或者传输；

反序列化，简单讲就是将json格式字符串转换成python字典，用于对其进行分析和处理。

JSON和DICT格式互转方法：

import json

# 序列化成json字符串

d = {‘name'：‘jod'}

j = json.dumps(d)

# 反序列化成字典

print json.loads(j)

而在requests库中，不用json.loads方法进行反序列化，而是提供了响应对象的json方法，用来对json格式的响应体进行反序列化

比如：

r = requests.get(url)

r.json()
***
requests模块中，r.json()为Requests中内置的JSON解码器

其中只有response返回为json格式时，用r.json()打印出响应的内容，

如果response返回不为json格式，使用r.json()会报错