def selection_sort(n, arr):
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

n = int(input("Enter the value of n: "))
arr = []
print("Enter the array elements: ")
for i in range(n):
    element = int(input())
    arr.append(element)
    
print("Array before Sorting:")
for i in arr:
    print(i,end=" ")
    
selection_sort(n, arr)
    
print("\nArray after Sorting in Ascending Order:")
for i in arr:
    print(i,end=" ")