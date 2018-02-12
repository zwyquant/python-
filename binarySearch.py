#二分查找法

def binarySearch(key,alist): 
    low = 0
    high = len(alist)-1

    while low <= high:
        mid = (low + high) // 2

        print (mid,alist[mid])
        
        if alist[mid] < key:
            low = mid + 1
        elif alist[mid] >key:
            high = mid - 1     

        else:
            return mid    
    return -1


def main():
    a=range(100)  
    print('关键字的索引位置是{}'.format(binarySearch(0,a)) )
    print('关键字的索引位置是{}'.format(binarySearch(51,a)) )
    print('关键字的索引位置是{}'.format(binarySearch(99,a)) )


if __name__ =='__main__':
    main()
