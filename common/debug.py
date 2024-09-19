import json

# 打开文件并读取内容
with open('../data/json.txt', 'r', encoding="utf-8") as file:
    data = file.read()

# 将JSON字符串转换为Python字典
data_dict = json.loads(data)

# 提取所有"id"字段的值并换行展示
ids = [item['id'] for item in data_dict['data']]
result = '\n'.join(ids)

# 打开文件并写入数据
with open('../data/sessionId.txt', 'w', encoding="utf-8") as file:
    file.write(result)