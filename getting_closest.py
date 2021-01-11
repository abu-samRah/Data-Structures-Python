class closest:
    def __init__(self, targetc):
        self.targetc = targetc


    def getclosest(self,arr1 ,arr2, target):
        closest = None
        intermediate = None
        for i in range(len(arr1)):
            for y in range(len(arr2)):
                if i == 0 and y ==0:
                    closest = arr1[i] + arr2[y]
                    
                else:
                    intermediate = arr1[i] + arr2[y]
                    x =  target - intermediate 
                    z =  target - closest 
                    if (intermediate < target):
                        closest = closest if z < x else intermediate
                    else:
                        closest = closest if z > x else intermediate
        return closest

if __name__ == '__main__':
    arr1 = [-1,3,8,2,9,5]
    arr2 = [4,1,2,10,5,20]
    ele = closest(24)
    print(ele.getclosest(arr1,arr2,-3))    
    