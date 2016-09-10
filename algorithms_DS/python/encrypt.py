'''
Write a function that takes a string, and encrypts it as follows:
find the most common three character sequence that appears in the string.
find a character that does not appear in the string
replace the sequence with the character everywhere it appears in the string,
then put them both at the beginning of the string so it's possible to get
the original back
Example:
press("Excellent bells ring pellucidly") -> "ellZExcZent bZs ring pZucidly"
'''
import string

def find_substrings(s):
    substrings = []
    for i in range(len(s) - 2):
        r = s[i : i+3]
        substrings.append(r)
    return substrings

def find_most_frequent(s):
    most_frequent = ('', 0)
    substrings = find_substrings(s)
    for sub in substrings:
        count = s.count(sub)
        if count > most_frequent[1]:
            most_frequent = (sub, count)
    return most_frequent[0]

def not_in_s(s):
    possible_characters = string.printable
    for ch in possible_characters:
        if ch not in s:
            return ch

def encrypt(s):
    most_frequent = find_most_frequent(s)
    missing_character = not_in_s(s)
    # hardcode missing_character for testing
    missing_character = 'Z'
    new_str = s.replace(most_frequent, missing_character)
    result = most_frequent + missing_character + new_str
    return result

if __name__ == '__main__':
    s = 'Agata and Rachel'
    print encrypt(s)

    # assert encrypt("Excellent bells ring pellucidly") == "ellZExcZent bZs ring pZucidly"
