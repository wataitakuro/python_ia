#関数の演習1
def fizzbuzz(a=1,b=100):
    for i in range(a,b+1):

        if i%15 == 0:
            print('FizzBuzz')
        elif i%5 == 0:
            print('Buzz')
        elif i%3 == 0:
            print('Fizz')
        else:
            print(i)
fizzbuzz()
