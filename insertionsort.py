# def insertionsort(l,arr):
#     for i in range(1,l):
#         temp=arr[i]
#         j=i-1
        
#         while j>=0 and temp<arr[j]:
#             arr[j+1]=arr[j]
#             j=j-1
#         arr[j+1]=temp


# arr=[7,2,9,1,6]
# l=len(arr)
# res=insertionsort(l,arr)
# print(arr)



def insertionsort(arr,l):

    for i in range(1,l):
        temp=arr[i]
        j=i-1

        while j>=0 and temp<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=temp




arr=[7,2,9,1,6]
l=len(arr)
res=insertionsort(l,arr)
print(arr)

