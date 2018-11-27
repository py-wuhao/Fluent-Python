import sys
import re

# 编译正则表达式模式，返回模式对象。
WORD_RE = re.compile(r'\w+')

index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # 这其实是一种很不好的实现，这样写只是为了证明论点
            # occurrences = index.get(word, [])
            # occurrences.append(location)
            # index[word] = occurrences
            # 在下面index.setdefault 返回的是列表 怎么添加到字典的？？？？
            index.setdefault(word, []).append(location)
            print('abc')
# 以字母顺序打印出结果
for word in sorted(index, key=str.upper):  # str.upper 是方法的引用
    print(word, index[word])
