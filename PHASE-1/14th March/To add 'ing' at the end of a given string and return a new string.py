#Practice4
#Python program to add 'ing' at the end of a given string and return a new string, if the given string already ends with 'ing' then add 'ly' and if the length of the given string is less than 3,leave it unchanged)
def add_ing(word):
    if len(word)<3:
        return word
    elif word[-3:]=='ing':
        return word+'ly'
    else:
        return word+'ing'

word1='sleep'
print(add_ing('sleep'))
word1='amazing'
print(add_ing('amazing'))
word1='is'
print(add_ing('is'))
