
class bubbleSort:

    def __init__(self, array):
        self.array = array
        self.length = len(array)

    def __str__(self):
        return " ".join([str(x)
                         for x in self.array])

    def iterBubbleSort(self, key='transaction_amount'):
        n = self.length
        for i in range(n):
         for j in range(0, n-i-1):

            if self.array[j][key] > self.array[j+1][key]:
                self.array[j], self.array[j+1] = self.array[j+1], self.array[j]

    def bubbleSortRecursive(self, n=None):
        if n is None:
            n = self.length

        
        if n == 1:
            return

        for i in range(n - 1):
            if self.array[i] > self.array[i + 1]:
                self.array[i], self.array[i +1] = self.array[i + 1], self.array[i]

        self.bubbleSortRecursive(n - 1)

def main():
    rec_array = [64, 34, 25, 12, 22, 11, 90]

    rec_sort = bubbleSort(rec_array)

    
    rec_sort.bubbleSortRecursive()
    print("Sorted array :\n", rec_sort)
    
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
    
    iter_sort = bubbleSort(elements)
    iter_sort.iterBubbleSort()
    print("Sorted array :\n", iter_sort)
    
if __name__ == "__main__":
    main()


