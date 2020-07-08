n = int(input("enter a number:  "))
(a,b) = (0,1)
for i in range(1,n):
    (a,b) = (a+b,b)
print(a + b)
