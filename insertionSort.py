def insertionSortIterative(arr): 
  
  for i in range(1,len(arr)):  
      x= i - 1
      y = i
      while(x>=0):
          if arr[y] < arr[x]:
              arr[y], arr[x] = arr[x] , arr[y]
              y=x
          x-=1

def insertionSortRec(arr,n): 
  
      if n <=1 :
          return
      insertionSortRec(arr,n-1)   
      
      x= n - 2 #1
      y = n-1 #2
      while(x>=0):
          if arr[y] < arr[x]:
              arr[y], arr[x] = arr[x] , arr[y]
              y=x
          x-=1  
  
  
# Driver code to test above 
if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    insertionSortIterative(elements)
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
        insertionSortRec(elements,len(elements))
        print(f'sorted array: {elements}')