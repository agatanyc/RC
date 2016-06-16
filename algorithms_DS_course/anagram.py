def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        for i in s1:
            r = False
            if i in s2:
                r = True
        return r

def is_anagram_2(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        for i in s1:
            if i not in s2:
                return False
        return True


assert is_anagram('bbaa', 'abab')
assert is_anagram_2('bbaa', 'abab')
    
