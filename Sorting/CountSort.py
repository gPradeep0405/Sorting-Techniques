def counting_sort(arr):
    maxx = max(arr)
    counts = [0] * (maxx + 1)

    for x in arr:
        counts[x] += 1
        
    i = 0
    for c in range(maxx + 1):
        while counts[c] > 0:
            arr[i] = c
            i += 1
            counts[c] -= 1

arr=list(map(int,input("Enter the element with seperate space:").split()))
counting_sort(arr)
print(arr)