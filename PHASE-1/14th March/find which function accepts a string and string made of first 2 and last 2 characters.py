#Practice3(find which function accepts a string and string made of first 2 and last 2 characters)
def function1(str1):
    length=len(str1)
    if length<2:
        return (-1)
    elif length==2:
        return (str1*2)
    else:
        return(str1[0:2]+str1[-2:])
str1=input()
print(function1(str1))
