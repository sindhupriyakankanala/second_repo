
#nested for loop

# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j,end="")
#     print()


# x=int(input("enter x value:"))
# y=int(input("enter y value:"))
# for i in range(1,x):
#     for j in range(1,y):
#         print(i*j,end="")
#     print()


#right triangle pattern

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("i={} and j={}".format(i,j))
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()


#rectangular pattern
# r=int(input("enter no of rows:"))
# c=int(input("enter no of coloumns:"))
# for i in range(r):
#     for j in range(c):
#         print("*",end="")
#     print()


# for i in range(1,6):
#     for j in range(1,6):
#         print(i,end="")
#     print()


# 1
# 21
# 321
# 4321
# 54321 

for i in range(1,6):
    for j in range(i,0,-1):
        print(i,end="")
    print()


# 5
# 45
# 345
# 2345
# 12345


# for i in range(5,0,-1):
#     for j in range(i,6):
#         print(j,end="")
#     print()



# k=0
# for i in range(5,0,-1):
#     for j in range(5-k,6):
#         print(j,end="")
#     k+=1
#     print()

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# k=1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k+=1
#     print()

# A
# A B
# A B C
# A B C D 
# A B C D E 

# for i in range(65,70):
#     for j in range(65,i+1):
#         print(chr(j),end=" ")
#     print()

# A 
# B C 
# D E F 
# G H I J 
# K L M N O 

# k=65
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k+=1
#     print()

# 5 4 3 2 1
# 4 3 2 1 
# 3 2 1
# 2 1
# 1

# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end="")
#     print()


# 12345
# 2345
# 345
# 45
# 5

# for i in range(1,6):
#     for j in range(i,6):
#         print(j,end="")
#     print()



