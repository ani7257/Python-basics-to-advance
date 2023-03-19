#Practice5
#String rotation
s=input().split(",")
stt=[]
num=[]
for i in s:
    s1,n=i.split(":")
    stt.append(s1)#stt=[rhdt,ghftd]
    num.append(n)#numm=[246,1246]
def rotate (ss,n):#ss=rhdt,n=246
    n=str(n)
    s=0
    for i in n:#
        s+=int(i)**2
    if s%2==0:
        return ss[-1]+ss[:-1] #rhdt t +rhd
    else:
        return ss[2:]+ss[:2] #ghftd ftdgh
for i in range(len(num)): #i=0
    print(rotate(stt[i],num[i]))
