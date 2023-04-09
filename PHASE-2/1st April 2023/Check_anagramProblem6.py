#Problem6
def check_anagram(str1, str2):
    if str1==str2:
        return False
    elif sorted(str1)==sorted(str2):
        return True
        
str1 = input("Enter the first word to check:")
str2 = input("Enter the second word to check:")
print(check_anagram(str1, str2))
