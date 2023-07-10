s=input("enter the string : ")
x=0
for i in s:
    print("the char at positive index",x,"is",i,"and at negative index",x-len(s),"is",i)
    x+=1