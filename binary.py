with open("binary", "bw") as binFi:
    for i in range(10):
        a = bytes(i)
        binFi.write(a)

with open("binary", "br") as bFi:
    for b in bFi:
        print(b)
