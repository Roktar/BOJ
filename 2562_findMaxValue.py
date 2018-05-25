def getSequence(data) :
    dataList = [ [i, int(n)] for i, n in enumerate(data) ]
    data = [ int(n) for n in data ]
    sz = len(data)

    maxValue = -1

    for n in data :
        if n > maxValue :
            maxValue = n

    # for i in range(sz) :
    #     for j in range(0, (sz-i)-1 ) :
    #         if data[j] > data[j+1] :
    #             data[j] += data[j+1]
    #             data[j+1] = data[j] - data[j+1]
    #             data[j] -= data[j+1]
    
    #maxValue = data[-1]
    for i in range(sz) :
        if dataList[i][1] == maxValue :
            print(maxValue)
            print(dataList[i][0]+1)
            break

inputList = []

for i in range(9) :
    inputList.append(input())
getSequence(inputList)