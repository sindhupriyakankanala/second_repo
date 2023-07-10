# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5


# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()


# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()

# 5 
# 4 5
# 3 4 5
# 2 3 4 5 
# 1 2 3 4 5

# for i in range(5,0,1):
#     for j in range(i,6):
#         print(j,end=" ")
#     print() 

x=5
sum=0
for i in range(x,0,-1):
    sum=sum+i
b=sum
for j in range(x+1):
    for k in range(j):
        b=b-1
        print(b+1,end=" ")
    print()


# 5 5 5 5 5
# 4 4 4 4 
# 3 3 3
# 2 2
# 1

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()

# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
    

# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

# for i in range(1,6,1):
#     for j in range(5-i+1):
#         print(i,end=" ")
#     print()
    

# A B C D E 
# A B C D 
# A B C 
# A B 
# A 


# for i in range(69,64,-1):
#     for j in range(65,i+1):
#         print(chr(j),end=" ")
#     print()

# a b c d e 
# a b c d 
# a b c 
# a b 
# a


# for i in range(101,96,-1):
#     for j in range(97,i+1):
#         print(chr(j),end=" ")
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

# 1 2 3 4 5
# 6 7 8 9 
# 10 11 12
# 13 14 
# 15


# k=1
# for i in range(5,0,-1):
#     for j in range(i):
#         print(k,end=" ")
#         k+=1
#     print()



# *
# * *
# * * *
# * * * *
# * * * *
# * * *
# * *
# *

# for i in range(4):
#     print("* "*(i+1)) 
# for i in range(4):
#     print("* "*(4-i))
# print()
 
#         *
#       * * 
#     * * *
#   * * * *
# * * * * *

# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
    

#         *
#       * * *
#     * * * * *
#   * * * * * * * 
# * * * * * * * * * 

# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
    

# * * * * *
#   * * * *
#     * * *  
#       * * 
#         *

# n=5
# for i in range(5):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

# sum=0

# for i in range(x,0,-1):
#     sum=sum+i
#     print(sum)