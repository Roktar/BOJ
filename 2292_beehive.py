def getPathCount(num) :
    if num <= 0 :
        return 0
    elif num == 1 :
        return 1
    else :
        base = 1
        n = 1
        while num > base : 
            base += (6*n)
            n += 1
        return n

print(str(getPathCount(int(input()))))
