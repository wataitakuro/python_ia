def hello():
    global a
    a= 1

a = 10
hello()
print(a)

class Character:
    name  = ''
    def speak(self, comment):
        print(self.name + ':' + comment)

#Characterのインスタンスを、taro変数に代入
taro = Character() #インスタンス化
taro.speak('ハロー
taro.first_name=''