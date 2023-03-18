#Practice1(finding the numbers and digits in the sentence)
def function(str1):
    l_count = 0
    d_count = 0
    for i in str1:
        if i.isalpha():
            l_count=l_count+1
        elif i.isdigit():
            d_count=d_count+1
        else:
            continue
    return[l_count,d_count]
#s=input()
#print(function(s))
print(function("Infosys 123"))
print(function("ABCEFG"))
