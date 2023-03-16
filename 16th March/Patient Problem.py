#Practice2
def medical(str1):
    dict1 = {}
    O=0
    P=0
    E=0
    for i in range(0, len(str1), 2):
        if str1[i+1]=='O':
            O=O+int(str1[i])
        if str1[i+1]=='P':
            P=P+int(str1[i])
        if str1[i+1]=='E':
            E=E+int(str1[i])

    if O>P:
        if O>E:
            print("OrthoPedics")
        else:
            print("ENT")
    else:
        print("Pediatrics")
str1=input().split(",")
medical(str1)
