# @Time : 2020/5/15 16:28 
# @Author : tongyue
import yaml

# 转化成字典，注意a: 1 冒号后面有空格
yaml_dict_data = yaml.load("""
a: 1
""",Loader=yaml.FullLoader)

print(yaml_dict_data)