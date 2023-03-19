#Practice6(To find the sum of the largest prime factors of each of nine consecutive numbers starts from n)
def prime (i):
    for j in range (2,i-1):
        if (i8j==0):
            return False
        return True
def fun (num):
    for i in range (num, 1,-1):
        if (prime (i) and num%i==0):
            return i

sum=0
num=int (input())
for i in range (num, num+9):
    sum+=fun (i)
print(sum)  
