#在列表中查找最大值或最小值

def max1(alist): 
    pos = 0
    iMax=alist[0]

    while pos<len(alist):
        if alist[pos] > iMax:
            iMax = alist[pos]
        pos += 1

    return iMax

def min1(alist): 
    pos = 0
    iMin=alist[0]

    for i in alist:
        if alist[pos] < iMin:
            iMin = alist[pos]

    return iMin


def main():
    a=[3,8,42,7,6,9,44,78,88,4,9,56,99,1]  
    print('最大的数是{}'.format(max1(a)) )
    print('最小的数是{}'.format(min1(a)) )


if __name__ =='__main__':
    main()
