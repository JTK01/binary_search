from bisect import bisect_left, bisect_right

N,x = map(int,input().split())
array = list(map(int,input().split()))

result = bisect_right(array,x) - bisect_left(array,x)
if result == 0:
    print('-1')
else:
    print(result)
