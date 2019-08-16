# Text-Similarity-in-Python


| Function                    | 計算方式                                                   | 備註                              |
|-----------------------------|------------------------------------------------------------|-----------------------------------|
| Levenshtein.Ratio           | r = (sum - ldist) / sum                                    |                                   |
| Levenshtein Distance        | 由一個字串轉為另一字串的最少操作次數，包含插入、刪除、替換 |                                   |
| Levenshtein.Hamming         | 兩個等長字串之間對應位置上不同字符的個數                   | 兩字串需相等                      |
| Levenshtein.jaro            |                                                            | 原用途為 人口普查 姓名比對        |
| Levenshtein.jaro_winkler    |                                                            | 起始部分就相同的字串 給更高的分數 |
| FuzzyWuzzy.partial_ratio    | 若一字串全部包含在另一字串中，則=100                       |                                   |
| FuzzyWuzzy.token_sort_ratio | 與Levenshtein Ratio 類似                                   | 忽略單辭順序 對標點符號敏感       |
| FuzzyWuzzy.token_set_ratio  |                                                            |                                   |

***
## Requirements

import Levenshtein  #pip install python-Levenshtein

import opencc

***
## USAGE



```chinese_similarity("name1", "name2", replace_variants = True, convert_to_tradition = True)``` 




https://github.com/contr4l/SimilarCharactor

https://github.com/EasyIME/PIME/issues/64

https://github.com/YahooArchive/KeyKey/blob/master/YahooKeyKey-Source-1.1.2528/DataTables/cj-ext.cin

https://www.logcg.com/zh-tw/archives/3211.html
