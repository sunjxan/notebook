https://juejin.cn/post/7028579355643265038
计算机无论如何都无法理解人类语言，它只会计算，不过就是通过计算，它让你感觉它理解了人类语言。
它面临文字的时候，都是要通过数字去理解的。所以，如何把文本转成数字，这是NLP中最基础的一步。

http://www.cnblogs.com/End1ess/p/16165854.html
分词器Tokenizer独立于模型存在，拥有词汇文件，词汇表，vocab_size，可以将id和token互相转换
tokenizer.tokenize 将字符串转换为token序列
tokenizer.encode 将字符串转换为id序列
tokenizer.decode 与encode相反
tokenizer.convert_ids_to_tokens [7270， 2128] -> ['长', '安']
tokenizer.convert_tokens_to_ids ['长', '安'] -> [7270， 2128]
tokenizer.convert_tokens_to_string ['长', '安'] -> '长安'
