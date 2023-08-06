import dadan

text = '厦门明天的天气怎么样'

words = dadan.seg(text)  # 分词
print(words)

pos = dadan.pos(words)  # 词性标注
print(pos)

