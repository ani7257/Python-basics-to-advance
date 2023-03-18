#Practice5(To check double numbers which accepts a whole number)
def check_double (number):
    num1=str(number*2)
    number=str(number)
    count=0
    for x in number:
        if x in num1:
            count+=1
        else:
            return False
    if count==len(number):
        return True
print(check_double (245))
print(check_double (125874))
