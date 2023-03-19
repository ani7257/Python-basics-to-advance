#Practice3(To tokenize the giving 5 sentences into words,excluding the stop words)
sentences=["a new world record was set","in the holy city of ayodhya","on the eve of diwali on tuesday","with over three lakh diya or earthen lamps","lits up simultaneously on the banks of the sarayu river"]
stopwords=['for','a','of','the','and','to','in','on','with','was']
result=[]
for sentence in sentences:#"a new world was set"
    row_data=[]
    for word in sentence.split():
        if word not in stopwords:
            row_data.append(word)#new world record set
    result.append(row_data)
print(result)

print([[word for word in sentence.split()
        if word not in stopwords]for sentence in sentences])
