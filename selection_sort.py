arr=[4,1,3,9,7]
for i in range(0,len(arr)):
    min_ele = i
    for j in range(i+1, len(arr)):
        if arr[min_ele] > arr[j]:
            min_ele = j
    arr[i], arr[min_ele] = arr[min_ele], arr[i]
for i in range(0, len(arr)):
    print(arr[i], end=" ")