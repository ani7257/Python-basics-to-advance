#Problem1
def product_of_three(n1, n2, n3):
    if n1==7:
        return n2*n3
    elif n2==7:
        return n3*n1
    elif n3==7:
        if n1!=7:
            return n1*2
        else:
            return 0
    else:
        return n1*n2*n3
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
n3=int(input("Enter third number: "))
product = product_of_three(n1,n2,n3)
if product==0:
    print("Note: No values can be included in the product.")
else:
    print("The product of the three numbers is:", product)

