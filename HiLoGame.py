import random
a = random.randint(1, 10)
print('Hello, I am Hi Lo game, I will choose a number and you guess !')
for i in range(5):
    while True:
        try:
            g = int(input('Enter your guess form 1 to 10 :'))
            if g < 11:
                break
            else:
                print("Only number from 1 to 10 allowed !")
        except:
            print("Only number from 1 to 10 allowed !")

    if g > a:
        print('the guess is higher than number')
    elif g < a:
        print('the guess is smaller than the number')
    elif g == a:
        print('You have guessed the number !')
        break
print('the number was ' + str(a))
