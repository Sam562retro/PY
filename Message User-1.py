def enter_message():
    f = open("new.dat","w")
    s = input("enter your message:  ")
    f.write(str(s))
    f.close()

def read():
    f = open("new.dat","r")
    g = f.read()
    print('system1:' + str(g))
    f.close()

def menu():
    print("1.new message")
    print("2.veiw message")
    i = int(input("enter a number:  "))
    if i == 1:
        enter_message()
    elif i == 2:
        read()
    menu()

if True:
    menu()
