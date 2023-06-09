#演習問題1
for i in range(1, 101):

    if i%15 == 0:
        print('FizzBuzz')
    elif i%5 == 0:
        print('Buzz')
    elif i%3 == 0:
        print('Fizz')
    else:
        print(i)

#演習問題2
for i in range(2, 101):
    is_prime = True
    for j in range(2, i):
        #print(f'i={i} j={j}')
        if i%j == 0:
            is_prime = False

    if is_prime:
        print(i)



