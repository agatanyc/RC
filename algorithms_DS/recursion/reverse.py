"""Write a function that takes a string as a parameter and returns a new string
that is the reverse of the old string."""

def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return reverse(s[1:]) + s[0]

if __name__ == '__main__':
    s = 'tamas'
    assert reverse(s) == 'samat'
