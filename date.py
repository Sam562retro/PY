import time
print(time.gmtime(0))
# for t in time.localtime():
#     print(t)
th = time.localtime()
print(th)
print("year: ", th[0])
print("month: ", th[1])
print("day: ", th[2])
print(time.time())
