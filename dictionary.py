import time
import sys

def new_word():
     
    w = str(input("enter the word you want to add: "))
    m = str(input("enter it's meaning: "))
    f = open('dict.dat','a')
    f.write(w + ':' + m + '\n')
    f.close()
def word_search():
     
    s = str(input('enter the word you want to search: '))
    f1 = open('dict.dat', 'r')
    for line in f1:
        if s in line:
            print(f1.readline())
    else:
        print('no such word!')
    f1.close()

def all_words():
     
    f2 = open('dict.dat','r')
    print(f2.read())
    f2.close()

def menu():
     
    print('Options: \n')
    print('1.add new word defination')
    print('2.check word defination')
    print('3.all words and meanings')
    print('4.exit')
    while True:
        try:
            choice = int(input('enter your choice:  '))
            if choice > 4 or choice == 0:
                print('only 1-4 numbers allowed!!!!!')
            else:
                break
        except:
            print('only numbers please!!!!!!!!')
    if choice == 1:
        new_word()
        time.sleep(1)
        menu()
    elif choice == 2:
        word_search()
        time.sleep(2)
        menu()
    elif choice == 3:
        all_words()
        time.sleep(3)
        menu()
    else:
        sys.exit(0)

def main():
    main()

if True:
    main()
