# chinese_name_similarity

Calculating the similarity between Chinese names.
***
## Requirements

```pip install python-Levenshtein```

```pip install opencc-python-reimplemented```

***
## Usage

### Basic
```chinese_name_similarity("name1", "name2")```


## Example Case
<img src="https://github.com/jasminehung/chinese_name_similarity/blob/master/testcase.JPG" alt="drawing" width="600"/>


2.	字串比對方法
function	計算方式	備註	是否使用
Levenshtein Ratio	r = (sum - ldist) / sum		O
Levenshtein Distance	由一個字串轉為另一字串的最少操作次數，包含插入、刪除、替換		O
Levenshtein Hamming	兩個等長字串之間對應位置上不同字符的個數	兩字串需相等	X
Levenshtein jaro_winkler	 
起始部分就相同的字串給更高的分數	X
Levenshtein Jaro	 
原用途為人口普查姓名比對	O
FuzzyWuzzy partial_ratio	若一字串全部包含在另一字串中，則=100		X
FuzzyWuzzy token_sort_ratio	與Levenshtein Ratio類似	忽略單辭順序
對標點符號敏感	O
FuzzyWuzzy token_set_ratio		忽略重複的單詞	X


