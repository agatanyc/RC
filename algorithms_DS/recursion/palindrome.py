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

def is_palindrome_sentence(s):
    if len(s) <= 1:
        return True
    else:
        sentence = ''
        for c in s:
            if c.isalnum():
                sentence += c.lower()
        if sentence[0] == sentence[-1]:
            return is_palindrome(sentence[1 : -1])
        else:
            return False

if __name__ == '__main__':
    s = 'abba'
    s2 = 'Able was I ere I saw Elba'
    assert is_palindrome(s)
    assert is_palindrome_sentence(s2)

