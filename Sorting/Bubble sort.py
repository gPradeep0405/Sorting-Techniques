arr = list(map(int,input().split("Enter number with spaces : ")))
n = len(arr)
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            # Swap elements
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)
