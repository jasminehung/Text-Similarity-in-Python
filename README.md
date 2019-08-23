# chinese_name_similarity

Calculating the similarity between Chinese names.
***
## Requirements

```pip install python-Levenshtein```

```pip install opencc-python-reimplemented```

***
## Usage

```chinese_name_similarity("name1", "name2")```

```chinese_name_similarity("name1", "name2", replace_variants = True, convert_to_tradition = True, family name = True)``` 

```chinese_name_similarity.custom("name1", "name2", replace_variants = 0.8, convert_to_tradition = 0.8)``` 

## Example Case
<img src="https://github.com/jasminehung/chinese_name_similarity/blob/master/testcase.JPG" alt="drawing" width="600"/>

***
## Dictionary


variant_mapping = {'啓':'啟','爲':'為','艷':'豔','裡':'裏','沉':'沈','晒':'曬','灑':'洒','祕':'秘','臺':'台','抬':'擡','檯':'台','梁':'樑','溼':'濕','汙':'污','闊':'濶','敘':'敍','峰':'峯','群':'羣','遍':'徧','匯':'滙','床':'牀','鋪':'舖','脣':'唇','蹤':'踪','蔥':'葱','憩':'憇','舉':'擧','鬥':'鬪','朵':'朶','卻':'却','腳':'脚','飆':'飇','秌':'秋','晳':'晰','咊':'和','飃':'飄','嶋':'島','𣑯':'桃','够':'夠','畧':'略','鵞':'鵝','讐':'讎','庵':'菴','霸':'覇','柏':'栢','背':'揹','杯':'盃','并':'併','鉢':'缽','布':'佈','册':'冊','厠':'廁','鏟':'剷','嘗':'嚐','場':'塲','耻':'恥','厨':'廚','糍':'餈','村':'邨','吊':'弔','叠':'疊','妒':'妬','珐':'琺','鰐':'鱷','况':'況','斂':'歛','渺':'淼','昵':'暱','娘':'孃','咽':'嚥','肴':'餚','鷄':'雞','捆':'綑','删':'刪','姗':'姍','栅':'柵','膳':'饍','膻':'羶','尸':'屍','謚':'諡','竪':'豎','嘆':'歎','掏':'搯','鑒':'鑑','奸':'姦','减':'減','杆':'桿','秆':'稈','雇':'僱','挂':'掛','鈎':'鉤','館':'舘','涌':'湧','恿':'慂','韵':'韻','衆':'眾','凶':'兇','綉':'繡','銹':'鏽','踪':'蹤','泄':'洩','糕':'餻','琅':'瑯','汚':'污','馱':'䭾','托':'託','潜':'潛','强':'強','棱':'稜','剋':'尅','届':'屆','灾':'災','蝎':'蠍','嫻':'嫺','綫':'線','厢':'廂','彦':'彥'}

similar_mapping = {'珮佩姵','偉瑋煒暐緯','祐佑','宥侑','庭廷','柏伯','宸辰','弘泓宏','紘竑','均鈞','璇嫙旋','琬婉','宛菀','螢瑩','翰瀚漢','亦羿奕弈','珊姍','俊峻竣駿','茿筑','臻蓁','諺彥','琪淇','建健','峰鋒','皓浩晧','萱宣','瑄暄煊','瑤媱','涵函','惠蕙','瑜愉媮渝','瑀禹','于予'}


## Reference

### Text-Similarity-in-Python

| Function                    | 計算方式                                                   | 備註                              |
|-----------------------------|------------------------------------------------------------|-----------------------------------|
| Levenshtein.Ratio           | r = (sum - ldist) / sum                                    |                                   |
| Levenshtein.Distance        | 由一個字串轉為另一字串的最少操作次數，包含插入、刪除、替換 |                                   |
| Levenshtein.Hamming         | 兩個等長字串之間對應位置上不同字符的個數                   | 兩字串需相等                      |
| Levenshtein.jaro            |                                                            | 原用途為 人口普查 姓名比對        |
| Levenshtein.jaro_winkler    |                                                            | 起始部分就相同的字串 給更高的分數 |
| FuzzyWuzzy.partial_ratio    | 若一字串全部包含在另一字串中，則=100                       |                                   |
| FuzzyWuzzy.token_sort_ratio | 與Levenshtein Ratio 類似                                   | 忽略單辭順序 對標點符號敏感       |
| FuzzyWuzzy.token_set_ratio  |                                                            |                                   |

### Websites
[contr4l/SimilarCharactor] (https://github.com/contr4l/SimilarCharactor)

[cj-ext.cin] (https://github.com/YahooArchive/KeyKey/blob/master/YahooKeyKey-Source-1.1.2528/DataTables/cj-ext.cin)

[從cns11643 中文標準全字庫生成倉頡和速成官方碼表](https://www.logcg.com/zh-tw/archives/3211.html)

[常見的異體字] (http://163.17.243.1/site4/table/2.htm)

### create python package
https://python-packaging.readthedocs.io/en/latest/minimal.html

https://packaging.python.org/tutorials/packaging-projects/


