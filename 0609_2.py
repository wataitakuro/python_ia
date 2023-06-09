#重複した値を消すのに、集合はよく使います。
number_list = [1, 1, 2, 3, 2, 5, 5, 6, 7, 7, ]
number_set = set(number_list)
print(number_set)

print('-----------------------------------')
#if 条件分:
number = 200

if number >100:
    print('100以上でした')
else:
    print('100以下でした')
#インデントエラーに気を付ける
print('処理を終わります')
#==(等しい)と!=(等しくない)はよく使うので覚えておくように。

print('-----------------------------------')
#in(含まれている)とnot in(含まれていない)も覚えておくように
namelist = {}
if 'taro' in namelist:
    print('taroはそこにいました')
else:
    print('taroはいませんでした')

a = 5
if a % 2 == 0:
     print(f'{a}は偶数です')
else:
     print(f'{a}は奇数です')

print('-----------------------------------')
#Pythonで、if　変数: と書いたときに、Falseとなるもの一覧
a = []
a = ''
a = 0
a = {}
a = ()
a = None
a = False

if a:
    print('aは空でした')
else:
    print('空じゃなかった')

name_list = ['鈴木', '佐藤', '山本', '渡辺']

for name in name_list:
    print(name)

for name in name_list:
    print(name, end=' ')
#間違ってfor文中に書かないように注意する
print('処理を終了します')

print('-----------------------------------')
#指定回数の繰り返しは、iという変数名を使うのが一般的、(5,101)で5以上101未満となる、(1,10,2)で1~9の数字を2つ飛ばしで入力する。
#この場合は、0から9まで入る(合計10)
for i in range(10):
    print(i)
print('-----------------------------------')
number_list = [12, 34, 5, 6, 32, 67, -3, 14, 35]

for number in number_list:
    if number < 0:
        print('処理を停止しました')
        break
    else:
        print(number)

print('-----------------------------------')
for number in number_list:
    if number <10:
        continue

dic = {
    '商品A':3,
    '商品B':10,
    '商品C':7,
    '商品D':5
}

print('商品一覧')
#辞書のkeysメソッドは、for key in ['商品A', '商品B', '商品C', '商品D']
for key in dic.keys():
    print(key)

print('\n商品と在庫数の一覧')
for key, value in dic.items():
    print('商品名:' + key + '\t在庫数:' + str(value))
















