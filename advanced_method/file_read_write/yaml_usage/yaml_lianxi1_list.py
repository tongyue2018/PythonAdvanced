# @Time : 2020/5/15 16:28 
# @Author : tongyue
import yaml

yaml_list_data = yaml.load("""
- Hesperiidae
- Papilionidae
- Apatelodidae
- Epiplemidae
""",Loader=yaml.FullLoader)

print(yaml_list_data)