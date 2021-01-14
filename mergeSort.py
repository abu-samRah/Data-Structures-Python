def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        l = arr[:mid]
        r = arr[mid:]
        mergeSort(l)
        mergeSort(r)
        i=j=k=0
        
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i +=1
            else:
                arr[k] = r[j]
                j +=1
            k +=1
        
        while i < len(l):
            arr[k] = l[i]
            i +=1 
            k +=1
            
        while j < len(r):
            arr[k] = r[j]
            j +=1 
            k +=1
 

# Driver code to test above 
if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    mergeSort(elements)
    print(elements)
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        mergeSort(elements)
        print(f'sorted array: {elements}')