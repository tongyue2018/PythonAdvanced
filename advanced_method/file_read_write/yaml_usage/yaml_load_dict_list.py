# @Time : 2020/5/15 16:28 
# @Author : tongyue
import yaml

# 文件注意- ：后面都有空格
yaml_file_data = yaml.load(open('yaml_data/yaml_data_2.txt'), Loader=yaml.FullLoader)

print(yaml_file_data)