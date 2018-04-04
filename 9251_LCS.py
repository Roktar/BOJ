def LCS(data1, data2) :
    outlist = list()
    outlist.append( [0] * (len(data1)+1) )

    maxCount, minCount = (data1, data2) if len(data1) >= len(data2) else (data2, data1)
    
    for i in range(1, len(maxCount)+1) :
        inlist = list()
        inlist.append(0)

        for j in range(1, len(minCount)+1) :
            if maxCount[i-1] == minCount[j-1] :
                inlist.append( outlist[0][j-1] +1 )
            else :
                inlist.append( outlist[0][j] if outlist[0][j] > inlist[j-1] else inlist[j-1] )
        
        outlist[0] = inlist
    return outlist[0][-1]

print( LCS(input(), input()) )