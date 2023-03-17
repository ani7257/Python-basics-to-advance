#Practice3
str1 = "I like Python"
str2 = "Java is a very popular language"
str1 = str1.replace(" ", "")
str2 = str2.replace(" ", "")
common = ""
for char in str1:
    if char in str2 and char not in common:
        common += char
if common == "":
    print(-1)
else:
    print(common)
