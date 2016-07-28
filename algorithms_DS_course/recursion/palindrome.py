"""Write a function that takes a string as a parameter and returns True if 
the string is a palindrome, False otherwise."""

def is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1 : -1])
        else:
            return False

if __name__ == '__main__':
    s = 'abba'
    assert is_palindrome(s)

