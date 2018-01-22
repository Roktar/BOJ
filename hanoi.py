def hanoi(a, b, c, N):
    if N == 1:
        print("%d %d" % (a, c))
    else:
        hanoi(a, c, b, N-1)
        print("%d %d" % (a, c))
        hanoi(b, a, c, N-1)

cnt = int(input())
moveCount = pow(2, int(cnt)) -1
print(moveCount)
if cnt <= 20 :
    hanoi(1, 2, 3, cnt)
