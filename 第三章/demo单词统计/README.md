1.enument(iterable,start)
    iterable:可迭代对象
    start：下标起始位置
    return：返回 enumerate(枚举) 对象。

2.setdefault(key,default=None)
原文：获取单词的出现情况列表，如果单词不存在，把单词和一个空列表
放进映射，然后返回这个空列表，这样就能在不进行第二次查找的情况
下更新列表了

若果key不存在就在字典中添加key和默认值，并返回默认值，原文返回列表（引用），所以append追加进去了值
