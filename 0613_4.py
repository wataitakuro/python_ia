#import モジュール名
#ファイルの先頭に、import文をまとめる
import fizzbuzz_func

#fizzbuzz_func.pyの、fizzbuzz関数を呼んでいる
fizzbuzz_func.fizzbuzz(1,100)

#from　モジュール名　import 関数やクラス
from fizzbuzz_func import fizzbuzz
fizzbuzz(1, 100)