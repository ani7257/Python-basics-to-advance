#Practice1(To find the even and odd part and if odd then square it and if it is even then cube it)
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#for loop --odd -->square it
#even -->cube it
result=[]
for row in mat:
    row_data=[]
    for ele in row:
        if ele%2!=0:
            row_data.append(ele**3)
        else:
            row_data.append(ele**2)
    result.append(row_data)
print(result)

#List Comprehension
print([ele**3 if ele%2!=0 else ele**2 for row in mat for ele in row])
print([[ele**2 if ele%2!=0 else ele**3 for ele in row] for row in mat])

