def binary_jae(array,target,start,end):
    if start > end:
        return None
    mid = (start + end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary(array,target,start,mid-1)
    else:
        return binary(array,target,mid+1,end)

def binary_ban(array,target,start,end):
    while(start <= end):
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

N, target = map(int,input().split())
array = list(map(int,input().split()))

result = binary_ban(array,target,0,N-1) #binary_jae & binary_ban both work!!
if result == None:
    print("찾는게 없네용~")
else:
    print(str(result + 1)+"번째에 있네용~")
