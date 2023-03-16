#Practice1(Palindrome_number)
def nearest_palindrome(num):
    def is_palindrome(n):
        return str(n)==str(n)[::-1]

    i=num+1
    while not is_palindrome(i):
        i+=1
    return i
print(nearest_palindrome(99))
print(nearest_palindrome(1221))
print(nearest_palindrome(121))

