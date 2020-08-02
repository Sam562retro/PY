import webbrowser as w
import time as t
import playsound as p
a = 30
b = 2
while True:
    for i in range(60):
        print(b,":",a,":",i)
        t.sleep(1)
    a+=1
    if a == 60:
        b+=1
        a=0
    if b == 2 and a == 31:
        w.open('https://mail.google.com/mail/u/0/#inbox',new=1)
        w.open('https://mail.google.com/mail/u/1/#inbox')
        w.open('https://classroom.google.com/u/1/c/NjgxNjM4Mzc4NTha')
        w.open('https://classroom.google.com/u/0/h')
        p("Twin-bell-alarm-clock.mp3")
        break
print("done")
