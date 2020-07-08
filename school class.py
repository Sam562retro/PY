import webbrowser as w
import winsound
w.open('https://mail.google.com/mail/u/0/#inbox',new=1)
w.open('https://mail.google.com/mail/u/1/#inbox')
w.open('https://classroom.google.com/u/1/c/NjgxNjM4Mzc4NTha')
w.open('https://classroom.google.com/u/0/h')
w.open("https://meet.google.com")
print(" SCHOOL CLASS !!!!!!!!! ")
while True:
    try:
        duration = 1000
        freq = 440
        winsound.Beep(freq, duration)
    except:
        break
