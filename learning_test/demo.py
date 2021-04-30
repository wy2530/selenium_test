import yaml

file = open('a.yml', encoding='utf-8')
                        # 取消警告的？？？
res = yaml.load(file, Loader=yaml.FullLoader)
print(res)  # 默认会打印成字典格式,

"""
当yml文件中只有
- a
- b
- c
的时候，会变成列表的形式，就不是字典了


-
 name:
"""
