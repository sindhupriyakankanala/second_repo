# append() function examples


# l=[]
# l.append("10")
# print(l)

# l=[]
# l.append(10)
# l.append("10")
# print(l)
# l.append("sindhu")
# print(l)

# l=[10,20,30]
# l.append("priya")
# print(l)

# l=[50,60,70]
# print(l.append("60"))
# print(l)

# l=[]
# l.append(50)
# l.append(60)
# l.append(15)
# print(l)



#insert() function examples



# list=[10,20,30]
# list.insert(2,40)
# print(list)

# list=[10,20,30,40]
# l=list.insert(-2,100)
# print(list)
# print(l)

# l=[1,2,3,4,5,6]
# l.insert(20,10)
# print(l)

# l=[1,2,3,4]
# l.insert(2,"abc")
# print(l)

# l=["ab","cd","ef","gh"]
# n=int(input("enter the number to be inserted: "))
# index_num=int(input("enter the index number"))
# if n%2==0:
#     l.insert(index_num,n)
#     print("the given number",n,"is inserted at index 2")
# else:
#     print("the given number is not inserted")
# print(l)



#remove() function examples


# l=[1,2,3,4,5,6,7,8,9]
# print(l.remove(2))
# print(l)

# l=[10,20,30,40,50,10,20]
# l.remove(10)
# print(l)

# l=["10","20","30"]       
# l.remove(10)
# print(l)                                  #value error bcoz 10 is not in the list

# l=list(range(5))
# n=int(input("enter the number: "))
# if n in l:
#     l.remove(n)
#     print("the number is removed")
# else:
#     print("the number is not removed")
# print(l)

# l=list(range(10))
# n=int(input("enter the number: "))
# l.remove(n)
# print(l)



# count() function examples


# l=[1,2,3,4,5,6,7]
# print(l.count(2))

# l=[1,2,3,1,2,3]
# print(l.count(1))

# l=[10,20,30,40,50]
# print(l.count(60))

# l=[1,2,3,4,4,4,5,6,7,8]
# print(l.count(4))
# print(l.count(2))
# print(l.count(9))

# l=['a','b,','c','d','e']
# print(l.count('c'))



# index() function examples


# l=[1,2,3,4,5]
# print(l.index(3))

# l=['a','b','c','d']
# print(l.index('c'))

# l=[10,20,30,40,50,60]
# print(l.index(60))                  #output:5
# print(l.index(70))                  # value error

# l=['sindhu','bindu','hindu']
# print(l.index('bindu'))

# l=['a','b','c','d']
# print(l.index('b'))



# extend() function examples


# l1=[1,2,3,4,5,6,7]
# l2=[10,20,30,40,50]
# l3=l1.extend(l2)
# print(l1)
# print(l2) 
# print(l3)

# l1=['sindhu','bindu']
# l2=['hindu','nandu']
# l2.extend(l1)
# print(l1)
# print(l2)

# l1=[10,20,30]
# l2=[100,200,300]
# l3=[1,2,3]
# l1.extend(l3)
# l2.extend(l3)
# print(l1)
# print(l2)
# print(l3)

# a=['a','b','c']
# b=['d','e','f']
# c=['g','h','i']
# a.extend(c)
# print(a)

# l=[1,2,3]
# l.extend([4,5,6])
# print(l)



# pop() function examples


# list=[1,2,3,4]
# l=list.pop()
# print(list)
# print(l)

# list.pop()
# print(list)

# list=[1,2,3,4,5,6]
# list.pop(2)
# print(list)

# list=['abc','def','ghi','jkl']
# list.pop()
# print(list)

# l=[1,2,3,4,5,6]
# l.pop(4)
# print(l)



# clear() function examples


# list=[1,2,3,4]
# list.clear()
# print(list)

# l=['sindhu','sunny','kittu']
# print(l.clear())
# print(l)

# fruits=['apple','grapes','cherry']
# print(fruits)
# fruits.clear()
# print(fruits)

# x=[10,20,30,40]
# x.clear()
# print(x)



#sort() function examples


# l=[2,3,1]
# print(l.sort())
# print(l)

# l=["1","a","2","b","3"]
# l.sort()
# print(l)

# l=['a','A',"97"]
# l.sort()
# print(l)

# a=['s','i','n','d','u']
# b=[6,8,3,0,5]
# #c=[10,"a",20,"b"]
# d=["a","20","b","40"]
# print(a)
# print(b)
# #print(c)
# print(d)
# a.sort()
# b.sort()
# #c.sort()
# d.sort()
# print(a)


# l=[12,34,60,76,60,12,97,'a']              #type error
# l.sort()
# print(l)



#reverse() function examples


# l=[10,20,30,40,10,20]
# print(l,"original list")
# l.reverse()
# print(l,"reversed list")

# l=['a','b','c','d',97]
# l.reverse()
# print(l)

# l=['sindhu',10,'python']
# l.reverse()
# print(l)

# l=['10',"a",20,"b"]
# print(l.reverse())
# print(l)

# l=['sindhu','priya']
# print(l.reverse())
# print(l)



#copy() function examples


# l=[10,20,30,40,"10","2","sindhu"]
# print(l.copy())
# print(l)