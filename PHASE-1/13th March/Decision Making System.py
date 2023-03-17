#Decision making statement
#read a number-->
#multiple of 3-->
#multiple of 5-->

num=int(input("Enter an integer number"))
print(num,type(num))
if(num%3==0 and num%5==0):
    print("Multiple of both 3 and 5")
elif(num%3==0):
    print("Multiple of 3")
elif(num%5==0):
    print("Multiple of 5")
else:
    print("Invalid")


