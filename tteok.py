def slice(array,H,M):
    cnt = 0
    for i in array:
        if i > H:
            cnt += (i - H)
    if cnt >= M:
        return True
    else:
        return False


N, M = map(int,input().split())
tteok = list(map(int,input().split()))

max = max(tteok)
start = 0
answer = 0
while max >= start:
    mid = (max + start) // 2
    result = slice(tteok,mid,M)
    if result == True:
        start = mid + 1
        answer = mid
    else:
        max = mid - 1
print(answer)
