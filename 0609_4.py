#関数の定義
def say_hello(a):
     print(a)
#関数の呼び出し
say_hello('こんにちは')

#placeが第一引数、weatherが第二引数
def message(s=None):
    if s is None:
        print('文字が未入力です')
    else:
        print('入力文字は' + s + 'です')
message()

def weather_report(place, weather):
    print('今日の' + place + 'の天気は' + weather + 'です')

weather_report('東京', '曇り')
weather_report('札幌', '晴れ')

def tax(price):
    tax = int(price * 0.1)
    return tax

a = tax(75)
b = tax(1980)
print(a)
print(b)

def cleaning(data, *args, **kwargs):


cleaning(
    '12月3日'

)
    staffs = ''
    for person in args





