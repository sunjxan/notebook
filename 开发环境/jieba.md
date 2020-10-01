```
pip3 install jieba
```

### 分词（Tokenize）
支持四种分词模式：

- 精确模式，试图将句子最精确地切开，适合文本分析；
- 全模式，把句子中所有的可以成词的词语都扫描出来, 速度非常快，但是不能解决歧义；
- 搜索引擎模式，在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词；
- paddle模式，利用PaddlePaddle深度学习框架，训练序列标注（双向GRU）网络模型实现分词。同时支持词性标注。paddle模式使用需安装paddlepaddle-tiny，pip install paddlepaddle-tiny==1.6.1。目前paddle模式支持jieba v0.40及以上版本。jieba v0.40以下版本，请升级jieba，pip3 install jieba --upgrade 

```
import jieba

str = '我来到beijing清华大学，我说：“hello, everyone!”。'

# 精确模式
'/'.join(jieba.cut(str))
# '我/来到/beijing/清华大学/，/我/说/：/“/hello/,/ /everyone/!/”/。'

# 全模式
'/'.join(jieba.cut(str, cut_all=True))
# '我/来到/beijing/清华/清华大学/华大/大学/，/我/说/：“/hello/,/ //everyone/!”。'

# 搜索引擎模式
'/'.join(jieba.cut_for_search(str))
# '我/来到/beijing/清华/华大/大学/清华大学/，/我/说/：/“/hello/,/ /everyone/!/”/。'
```

### 词性标注（Part-Of-Speech tag, POS-tag）

实词是含有实际意义的词，实词能单独充当句子成分，即有词汇意义和语法意义的词：
1. 名词：表示实体和概念名称的词
    - n 普通名词
    - nr 人名
    - ns 地名
    - nt 机构名
    - nw 作品名
    - nz 其它专名

2. 代词：在句子结构中代替其他词的词
    - r 代词

3. 动词：表示动作的词
    - v 普通动词
    - vd 动副词
    - vn 名动词
   
4. 形容词：修饰名词，表示人或事物的性质、状态、特征或属性的词
    - a 形容词
    - ad 副形词
    - an 名形词

5. 数词：表示数量（基数词）和序数（序数词）的词
    - m 数词

6. 量词：表示数量单位的词
    - q 量词

7. 区别词：通常有一个反义词，表示互相对立的两种属性之一
    - b 区别词


虚词是没有完整意义的词汇，但有语法意义或功能的词：
1. 副词：修饰动词，表示动作的特征，状态等的词
    - d 副词

2. 介词：用在句子的名词成分之前，说明该成分与句子其它成分关系的词
    - p 介词

3. 连词：连接两句话，表示其中逻辑关系的词
    - c 连词

4. 助词：表示语气，句子结构和时态等语法和逻辑性的词
    - u 助词

5. 其他虚词
    - xc 叹词、拟声词等


其他标签
1. 时间
    - t
2. 处所词
    - s
3. 方位词
    - f
4. 英文
    - eng
5. 无法识别
    - x

```
import jieba.posseg as pseg

str = '我来到beijing清华大学，我说：“hello, everyone!”。'

list(pseg.cut(str))
# [pair('我', 'r'), pair('来到', 'v'), pair('beijing', 'eng'), pair('清华大学', 'nt'), pair('，', 'x'), pair('我', 'r'), pair('说', 'v'), pair('：', 'x'), pair('“', 'x'), pair('hello', 'eng'), pair(',', 'x'), pair(' ', 'x'), pair('everyone', 'eng'), pair('!', 'x'), pair('”', 'x'), pair('。', 'x')]
```

### 载入词典

- 开发者可以指定自己自定义的词典，以便包含 jieba 词库里没有的词。虽然 jieba 有新词识别能力，但是自行添加新词可以保证更高的正确率
- 用法： `jieba.load_userdict(file_name)` # file_name 为文件类对象或自定义词典的路径
- 词典格式和 `dict.txt` 一样，一个词占一行；每一行分三部分：词语、词频（可省略）、词性（可省略），用空格隔开，顺序不可颠倒。`file_name` 若为路径或二进制方式打开的文件，则文件必须为 UTF-8 编码。
- 词频省略时使用自动计算的能保证分出该词的词频。

```
创新办 3 i
云计算 5
凱特琳 nz
台中
```

### 调整词典

- 使用 `add_word(word, freq=None, tag=None)` 和 `del_word(word)` 可在程序中动态修改词典。
- 使用 `suggest_freq(segment, tune=True)` 可调节单个词语的词频，使其能（或不能）被分出来。
- 注意：自动计算的词频在使用 HMM 新词发现功能时可能无效。

### 删除停用词

在处理语料时，需要删除停用词。所谓停用词就是对理解中文含义没有明显作用的哪些单词，常见的停用词举例如下：

	一一  
	一下  
	一个  
	一些  
	一何  
	一切  
	一则  
	一则通过  
	一天  
	一定  
	一方面  
	一旦  
	一时 

另外所有的字母和数字还有标点符号也可以作为停用词。我们把停用词保存在一个文本文件里面便于配置使用。
```
# 定义加载停用词的函数

def load_stopwords():
	with open("stopwords.txt") as F:
	    stopwords=F.readlines()
	return [word.strip() for word in stopwords]

# 使用停用词过滤之前提取的文本内容

stopwords = load_stopwords()
    
x = [ [word for word in line.split() if word not in stopwords] for line in x]
```

### 基于 TF-IDF 算法的关键词抽取

```
# 基本思想:
# 将待抽取关键词的文本进行分词，取出中文词和英文词，并剔除停止词
# 计算每个词的TF频率值
# 字典idf_freq中保存中文词的IDF值：ln(1/DF)
# 取每个词的IDF值：从字典idf_freq中取值，如果没有，取median_idf值
# 相乘得到TF-IDF值

import jieba.analyse

# sentence 待提取的文本
# allowPOS 关键词的词性范围，默认值为空，即不筛选
# topK 取TF-IDF值最大的前K个词，默认值为 20
# withWeight 是否返回TF-IDF值
# withFlag allowPOS不为空时，是否返回词性，allowPOS为空时不返回
# jieba.analyse.extract_tags(sentence, allowPOS=(), topK=20, withWeight=False, withFlag=False)

str = '我来到beijing清华大学，我说：“hello, everyone!”。'
jieba.analyse.extract_tags(str, withWeight=True)

# 设置停止词
jieba.analyse.set_stop_words(stop_words_path)

# 继承jieba.analyse.TFIDF
class MyTFIDF(jieba.analyse.TFIDF):
    def __init__(self):
        super().__init__()
```

### 基于 TextRank 算法的关键词抽取

```
# 基本思想:
# 将待抽取关键词的文本进行分词，取出中文词
# 以固定窗口大小(默认为5，通过span属性调整)，词之间的共现关系，构建图
# 计算图中节点的PageRank，注意是无向带权图

import jieba.analyse

# sentence 待提取的文本
# allowPOS 关键词的词性范围，默认值为空，即不筛选
# topK 取TextRank值最大的前K个词，默认值为 20
# withWeight 是否返回TextRank值
# withFlag 是否返回词性
# jieba.analyse.textrank(sentence, allowPOS=(), topK=20, withWeight=False, withFlag=False)

str = '永和服装饰品有限公司'
jieba.analyse.textrank(str, withWeight=True, withFlag=True)

# 设置停止词
jieba.analyse.set_stop_words(stop_words_path)

# 继承jieba.analyse.TextRank
class MyTextRank(jieba.analyse.TextRank):
    def __init__(self, span=20, word_min_len=2):
        super().__init__()
        # 窗口大小
        self.span = span
        # 单词的最小长度
        self.word_min_len = word_min_len

    # 过滤条件，定义后其他限制（allowPOS、stop_words）失效
    def pairfilter(self, wp):
        return wp.flag not in ('x',) and wp.word not in self.stop_words and len(wp.word) >= self.word_min_len
```

