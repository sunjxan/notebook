https://juejin.cn/post/7028579355643265038
计算机无论如何都无法理解人类语言，它只会计算，不过就是通过计算，它让你感觉它理解了人类语言。
它面临文字的时候，都是要通过数字去理解的。所以，如何把文本转成数字，这是NLP中最基础的一步。

http://www.cnblogs.com/End1ess/p/16165854.html
分词器Tokenizer独立于模型存在，在录入语料库后，有了词汇表，vocab_size，基本工作：分词、标记化
加载分词器要有vocab文件和配置json文件支持

tokenizer.tokenize 将字符串转换为token序列

tokenizer.convert_tokens_to_string ['长', '安'] -> '长安'
tokenizer.convert_ids_to_tokens [7270， 2128] -> ['长', '安']
tokenizer.convert_tokens_to_ids ['长', '安'] -> [7270， 2128]

tokenizer.encode 将字符串转换为id序列 tokenize + convert_tokens_to_ids
tokenizer.decode 将id序列转换为字符串 convert_ids_to_tokens + convert_tokens_to_string

以max_seq_length作标准，将序列填充或截断，填充使用的token是[PAD]，从左或从右。
统一长度的序列，就是NLP要的素材。
