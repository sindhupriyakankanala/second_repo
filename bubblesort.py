

def bubblesort(arr,l):
    for i in range(l):
        for j in range(i+1):
            if arr[i]>arr[j]:
                arr[i]=arr[j]
                j+=1
                

                
arr=[3,0,5,6]
l=len(arr)
res=bubblesort(arr,l)
print(arr)
