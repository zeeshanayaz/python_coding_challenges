# Check Palindrome – Is a string or number the same forward and backward?

def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("mom"))