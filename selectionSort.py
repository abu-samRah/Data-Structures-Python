def selectionSortIter(arr):
    
    for i in range(len(arr)-1):
            index= i
            for j in range(i +1,len(arr)): 
                if arr[j] < arr[index]:
                    index = j
            arr[index],arr[i] = arr[i], arr[index]

def minIndex(array,index,lenght):
    if index == lenght:
        return index
    
    current_index = minIndex(array,index+1,lenght)
    return index if array[index]<array[current_index] else current_index


def selectionSortRec(array,lenght,index=0):
    if lenght == index:
        return 
    
    min_Index = minIndex(array,index,lenght-1)
    
    array[index] ,array[min_Index] = array[min_Index], array[index]
    
    selectionSortRec(array,lenght,index+1)
    
  
# Driver code to test above 
if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    selectionSortIter(elements)
    print(elements)
    #
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        selectionSortRec(elements, len(elements))
        print(f'sorted array: {elements}')