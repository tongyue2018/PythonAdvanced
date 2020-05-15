# @Time : 2020/5/15 16:28 
# @Author : tongyue
import yaml

# 转化成字典，注意a: 1 冒号后面有空格
yaml_file_data = yaml.load(open('yaml_data/yaml_data_1.txt'), Loader=yaml.FullLoader)

print(yaml_file_data)