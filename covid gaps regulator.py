import webbrowser
def record():
    n = input('enter row with 0 as empty spaces and 1 with full spaces: ')
    p = input('enter place name: ')
    c = 0
    for i in range(len(n)):
        a = n[i]
        if a == '0':
            c += 1
            if c>=6:
                u = True
            else:
                u = False
        elif a == '1':
            c = 0
        else:
            break
    if u == False:
        h = 'NO'
    elif u == True:
        h = 'YES'
    print('6 feet gaps are being followed: ', u)
    f = open('covidgap.dat','a')
    f.write('\nplace name: ')
    f.write(p)
    f.write('\n6 feets gaps bieng folowed: ')
    f.write(h)
    f.close()


def menu():

    while True:
        try:
            print('\n\n\n\n\t\t\t\tWELCOME TO THE COVID-19 GAPS RECORDER FOR CITIES OR OTHER PLACES\n\n')
            print('1.view all records')
            print('2.enter another record')
            print('3.government live help desk through whatsapp')
            print('4.exit')
            j = input('\nenter the number you want to visit: ')
            if j == 1:
                f = open('covidgap.dat','r')
                print(f.read())
                time.sleep(2)
                menu()
                break
            elif j == '2':
                record()
                time.sleep(2)
                menu()
                break
            elif j == '3':
                print('loading...')
                time.sleep(1)
                print('oppening...')
                webbrowser.open("https://api.whatsapp.com/send?phone=919013151515&text=&source=&data=&app_absent=")
                break
            elif j == '4':
                return j
                break
            else:
                print('not an option')
        except:
            print('not an option only 1-4 numbers')




def welcome_screen():
    print('\t\t\t\t\tWELCOME TO THE COVID-19 GAPS RECORDER FOR CITIES OR OTHER PLACES')
    print('loading.....')
    time.sleep(2)

def main():
    welcome_screen()
    while True:
        menu()
        if menu.j == 4:
            break

if True:
    main()
