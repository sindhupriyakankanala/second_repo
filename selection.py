
def selectionsort(arr,l):
    for i in range(l):
        minindex=i
        for j in range(i+1,l):
            if arr[j]<arr[minindex]:
                minindex=j
        arr[i],arr[minindex]=arr[minindex],arr[i]
     



arr=[8,3,9,1,2]
l=len(arr)
res=selectionsort(arr,l)
print(arr)
