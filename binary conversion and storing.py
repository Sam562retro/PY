a = 65534      #FF FE
b = 65535      #FF FF
c = 65536      #00 01 00 00
d = 2998302    #00 2D C0 1E

with open("binary2", "bw") as binF:
    binF.write(a.to_bytes(2, 'big'))
    binF.write(b.to_bytes(2, 'big'))
    binF.write(c.to_bytes(4, 'big'))
    binF.write(d.to_bytes(4, 'big'))
    binF.write(d.to_bytes(4, 'little'))

with open("binary2", "br") as binFi:
    e = int.from_bytes(binFi.read(2), 'big')
    print(e)
    f = int.from_bytes(binFi.read(2), 'big')
    print(f)
    g = int.from_bytes(binFi.read(4), 'big')
    print(g)
    h = int.from_bytes(binFi.read(4), 'big')
    print(h)
    i = int.from_bytes(binFi.read(4), 'little')
    print(i)
