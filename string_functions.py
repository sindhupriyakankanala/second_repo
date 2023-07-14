#find() function examples


# str="am not available for the day"
# print(str.find("for"))   #output:17


# str="sindhu is working in marolix"
# if(str.find("u",10,19))==-1:
#     print("given substring is not found in main string")
# else:
#     print()


# substring=input("enter the substring: ")
# str="hello sindhu,are u ok now"
# if substring in str:
#     print(str.find(substring))
# print()                      #output:6


# str1="welcome to python programming language"
# str2=str1.find("t")
# str3=str1.find("t",25)
# print(str2)                  #output:8
# print(str3)                  #      -1



# str="kittu waste his time because he dont know time value"
# print(str.find("time"))        #output:16 because find() always returns returns the index of first occurance


# str="sindhu, sindhu, sindhu, sindhu, Sindhu"
# substring="sindhu"
# count=0
# start_index=0
# for i in range(len(str)):
#     j=str.find(substring,start_index)
#     if(j!=-1):
#         start_index=j+1
#         count+=1
# print("total occurances are: ",count)



#index() function examples



# str="hi hello good morning"
# print(str.index("hello"))           #output:3


# str="hi hello good morning"
# print(str.index("is"))              #output:exception



# substring=input("enter the substring: ")
# str="hi hello good morning good evening"
# if substring in str:
#     index_num=str.index(substring)
#     print(index_num)
#     if index_num%2==0:
#         print("index number is even number")
#     else:           
#         print("index number is odd number")                                  
#     print()                                           


# str1="welcome to python programming language"
# str2=str1.index("t")
# #str3=str1.index("t",25)
# print(str2)                  #output:8
# #print(str3)                  #      -1



#strip() function examples


# city=input("enter the city: ") 
# list=["hyd","wrgl","hnk","goa","shimla"]
# if city in city.strip("list"):
#     print("network connection available")
# else:
#     print("network connection not available")


# str="  hello good morning  "
# stripped_str=str.strip()
# print(stripped_str)


# str="sindhupriya"
# print(str.rstrip("s"))


# str="i hate you"
# print(str.strip("w"))


# str="   delhi is the capital of india   "
# print(str.rstrip())


# str="Abcdefghi"
# print(str.strip("a"))      #output:Abcdefghi bcoz strip() is case sensitive


# str="    today is today   "
# print(str)
# print(str.strip())
# print(str.strip("today"))



#rfind() function examples



# str="if she want to be like that let her be like that"
# print(str.rfind("like"))                           #output:39


# str="if she want to be like that let her be like that"
# print(str.rfind("t"))                                #output:47


# str="Nothing is impossible"
# print(str.rfind("u"))                                 #output:-1


# str="sindhu is working in marolix"
# if(str.rfind("u",10,19))==-1:
#     print("given substring is not found in main string")
# else:
#     print()



#count() function examples



# str="i will come,so u come there"
# print(str.count("come"))                    #output:2

# str="i will help you,u help me"
# print(str.count("help",11,120))             #output:1

# str="Krishnaaaaaaa"
# print(str.count("a"))                          #output:7

# str="drinking alcohol is injurious to health"
# print(str.count("at"))                             #output:0

# str="where is there is a ray,there is a way"
# print(str.count("is a ray"))                       #output:1


 
#split() function examples



# str="i will be waiting"
# print(str.split())                 #output ['i', 'will', 'be', 'waiting']

# str="i will be waiting"
# print(str.split("will"))             #output: ['i', 'be waiting']

# str="sindhu priya"
# print(str.split("i"))                    #output: ['s', 'ndhu pr', 'ya']

# str="come,go,new,old"
# print(str.split(",",2))                  #output: ['come', 'go', 'new,old']

# str="old is gold"
# print(str.split("o",3))                    #output: ['', 'ld is g', 'ld']

# s="10,20,30,40"
# print("-".join(s.split(",")))                #output: 10-20-30-40



#replace() function examples



# s="never give up"
# print(s.replace("e","a"))                   #output: navar giva up

# s="welcome home"
# print(s.replace("el","i"))                    #output: wicome home

# s="i like to play cricket"
# print(s.replace("cricket","hockey"))

# s="one two three one one two three"
# print(s.replace("one","only",2))



#rsplit() function examples



# s="rose lotus, jasmine"
# print(s.rsplit(", "))

# s="rose lotus jasmine"
# print(s.rsplit())

# s="abcdefgbh"
# print(s.rsplit("b",1))

# s="specially"
# print(s.rsplit("l",1))

# s="abc,def,ghi"
# print(s.rsplit(",",1))



#lower() function eaxamples



# s="AbcDefGhi"
# print(s.lower())

# s="SINDHU"
# print(s.lower())

# s=" I Hate You"
# print(s.lower())

# s="ABC002345A"
# print(s.lower())

# s="2345667"
# print(s.lower())



#upper() function examples



# s="Kankanala"
# print(s.upper())

# s="Kankanala 123 Sindhu"
# print(s.upper())

# s="Kankanala#$%"
# print(s.upper())

# s="KaNkAnaLa"
# print(s.upper())

# s="994919"
# print(s.upper())

 

#capitalize() function examples



# s="ramaseetha"
# print(s.capitalize())

# str="tomorrow is holiday"
# print(str.capitalize())

# str="Today Is Thursday"
# print(str.capitalize())

# str="my Number is 123"
# print(str.capitalize())



#casefold() function examples



# str="Lower Upper"
# print(str.casefold())

# str="1234 I LikE SWEEts"
# print(str.casefold())

# str="thank You for INviting"
# print(str.casefold())

# str="LowerCase12##"
# print(str.casefold())



#title() function examples



# s="thE earTH"
# print(s.title())

# s="thE sun sHinE 345"
# print(s.title())

# s="this is AN APPLE "
# print(s.title())



# isupper() function examples


# str="Sindhupriya"
# print(str.isupper())      #false

# str="SINDHU"
# print(str.isupper())            #true



#islower() function examples



# str="Sindhupriya"
# print(str.islower())        #false


# str="sindhu"
# print(str.islower())          #true



#center() function examples



# str="sindhu"
# print(str.center(10,"#"))           #    ##sindhu##



#endswith() function examples



# str="today is not a holiday"
# print(str.endswith("holiday"))        #true


# str="today is not a holiday"
# print(str.endswith("y"))               # true

# str="today is not a holiday"
# print(str.endswith("is"))                 # false



#expandtabs() funtion examples



# str="Ram\tis\ta\tgood\tboy"
# print(str.expandtabs(4))



#isalnum function examples


# str="abcdefgh1234"
# print(str.isalnum())                     #true

# str="abcdefghi"
# print(str.isalnum())                       #true

# str="1234"
# print(str.isalnum())                      #true

# str="1234@#$"
# print(str.isalnum())                      #false

# str="sindhu1234#$%"
# print(str.isalnum())                        #false



#join() function examples



# str=["abc","def","ghi","jkl"]
# print(" ".join(str))

# str=["abc","def","ghi","jkl"]
# print("*".join(str))

# str=["s","i","n","d","h","u"]
# print("*".join(str))



#isnumeric() function examples



# str="abcd345ghi"
# print(str.isnumeric())                  #false

# str="12345@#$"
# print(str.isnumeric())                  #false

# str="123456"
# print(str.isnumeric())                  #true

# str="sindhu"
# print(str.isnumeric())                    #false



#isspace()function examples



# s="sindhu priya "
# print(s.isspace())                           #false

# s="  "
# print(s.isspace())                           #true



#swapcase() function examples



str="Sindhu pRIYA"
print(str.swapcase())         

str="sindhu 1234"
print(str.swapcase())         

str="SINDHU 123#$%"
print(str.swapcase())         