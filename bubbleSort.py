#冒泡算法:对元素两两比较,大的数沉到后面,比较小的数就像气泡一样浮上一个位置. 最简单的排序算法

def bubbleSort(a):
    for i in range(len(a)-1,0,-1): #循环次数
        for j in range(i): #列表内循环
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]

def main():
    a=[3,8,42,7,6,9,44,78,88,4,9,56]  #要求按升序排列
    bubbleSort(a)
    print(a)

if __name__ =='__main__':
    main()
