def LengthRec(set1, a, n, k): 
    if (k == 0) : 
        if 'bb' in a:
            pass
        elif 'b' not in a:
            pass
        else:
            print(a)
        return
    for i in range(n): 
        b = a + set1[i] 
        LengthRec(set1, b, n, k - 1) 
  
def main():
        set1 = ['a', 'b'] 
        k = int(input("enter the number needed:  "))
        n = len(set1)
        LengthRec(set1, "", n, k )  

if True:    
    main()
  
