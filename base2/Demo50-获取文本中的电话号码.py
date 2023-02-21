# 代表一段文本内容
comtent ="""
    bbai1345678,huanhe13753789034
    yuqy123456,
"""

import re
# r取消转义 1 以1开头，【3-9】,第二位以3-9的范围内 \d{9} 后面9位都是数字
patten = r"1[3-9]\d{9}"

result = re.findall(patten,comtent)

for res in result:
    print(res)