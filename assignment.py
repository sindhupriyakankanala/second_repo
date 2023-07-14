
#input: ram is good boy
#output: boy good is ram

# str="ram is good boy"
# print("input string is: ",str)
# words=str.split(" ")

# words2=words[-1::-1]

# output=" ".join(words2)
# print("output string is: ",output)



#input: ABCDAABBCCDDEEFFGGHI
#output: ABCDEFGHI


# str="ABCDAABBCCDDEEFFGGHI"
# print("input string: ",str)
# list=[]
# for char in str:
#     if char not in list:
#         list.append(char)

# output_str="".join(list)
# print("output string: ",output_str)
    


str="ABCDAABBCCDDEEFFGGHI"
print("input string: ",str)
str2=""
for char in str:
    if char not in str2:
        str2=str2+char
print("output string: ",str2)

    
