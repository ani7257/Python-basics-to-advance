#Practice 1
'''n1=int(input())
n2=int(input())
n3=int(input())
if n1==7:
   print(n2*n3)
elif n2==7:
    print(n3)
elif n3==7:
    print("-1")
else:
    print(n1*n2*n3)'''

#Practice 2
'''def currencycal(INR,curr):
    if curr=="Euro":
        print("Amount", INR*0.01417)
    elif curr=="British Pound":
        print("Amount", INR*0.0100)
    elif curr=="Australian Dollar":
        print("Amount", INR*0.02140)
    elif curr=="Canadian Dollar":
        print("Amount", INR*0.02027)
    else:
        print(-1)
currencycal(300,"Euro")
currencycal(300,"British Pound")
currencycal(300,"Australian Dollar")
currencycal(300,"Canadian Dollar")'''

#Practice 3
'''adult_rate = 37550.0
child_rate = adult_rate / 3
service_tax = 0.07

num_adults = int(input("Enter the number of adults: "))
num_children = int(input("Enter the number of children: "))

total_cost = (adult_rate * num_adults) + (child_rate * num_children)
total_cost += total_cost * service_tax
total_cost *= 0.9 # apply 10% discount

print("Total ticket cost: Rs. {:.2f}".format(total_cost))'''

                    #OR

'''n_adults=int(input("Enter the number of adults:"))
n_childs=int(input("Enter the number of child:"))
total=((n_adults*37550.0)+((n_childs*37550.0)/3))
print(total)
total1=total*0.07
total2=total+total1
print("With your service tax",total2)

total_amount=total2*0.90
print(total_amount)'''

                    #OR

'''n_adults=int(input("Enter the number of adults:"))
n_childs=int(input("Enter the number of child:"))
total=(((n_adults*37550.0)+((n_childs*37550.0)/3))*1.07)*0.90
print(total)'''

#Practice 4
x=int(input("Enter the 5 rs coin:"))
y=int(input("Enter the 1 rs coin:"))
z=int(input("Amount to be Made:"))
print(z//5)
if ((y+5*x)>=z):
    print("5 rs coin needed:",z//5)
    print("1 rs coin needed:",z-(x*5))
else:
    print("-1")






