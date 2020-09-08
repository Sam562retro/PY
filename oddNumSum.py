g = int(input("Please enter the number till which you want the sum of odd primes."))
def checkPrime(i):
    z = 0
    for j in range(1, i + 1):
        if i % j == 0:
            z += 1
    if z == 2:
        return True
    else:
        return False
a = 0
for i in range(1, g):
    if i % 2 == 1:
        if checkPrime(i):
            a += i

print(a)
