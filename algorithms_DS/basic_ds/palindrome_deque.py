"""Palindrome-Checker"""
from deque import Deque

def is_palindrome(s):
    d = Deque()
    for c in s:
        d.add_front(c)

    size = float(d.size()) / 2
    if size % 2 == 0:
        for i in range(int(size)):
            if d.remove_front() == d.remove_rear():
                return True
        return False
    else:
        new_size = size / 2 + 1
        for i in range(int(new_size)):
            if d.remove_front() == d.remove_rear():
                return True
        return False

if __name__ == '__main__':
    p1 = 'radar'
    p2 = 'toot'
    p3 = 'madam'

    assert is_palindrome(p1)
    assert is_palindrome(p2)
    assert is_palindrome(p3)
    
