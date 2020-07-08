p = int(input())
q = int(input())
while True:
    if int(p)>int(q):
        while True:

            if int(p) == int(q):
                print(p+q)
                break
            elif int(q)>int(p):
                q = q-p
                if q == p:
                    print(p+q)
                    break
                elif int(p)>int(q):
                    p = p-q
                else:
                    continue
            else:
                p = p-q
        break
    elif int(q)>int(p):
        while True:
            if int(q) == int(p):
                print(q+p)
                break
            elif int(p)>int(q):
                p = p-q
                if p == q:
                    print(p+q)
                    break
                elif int(q)>int(p):
                    q = q-p
                else:
                    continue
            else:
                q = q-p
        break
    elif p == q:
        print(q+p)
        break
    else:
        break
