# @Time : 2020/5/15 16:28 
# @Author : tongyue
import yaml


# 加载字典
dict_data = {"a":[1,2]}
print(yaml.dump(dict_data))

with open('yaml_data/yaml_data_3.txt',mode='w') as f:
    yaml.dump(data=dict_data,stream=f)