'''
Write a function that takes two strings, and returns the number of times
the first string appears in the second, without using any of your
language's string processing facilities (i.e., treat the strings as 
lists of characters).

matches(['baba', 'abababa'])
-> 2
'''


def matches(stack, needle):
    count = 0
    for i in range(len(stack) - (len(needle) - 1)):
        if stack[i] == needle[0]:
            for j in range(1, len(needle) - 1):
                if stack[i + 1] != needle[j]:
                    break
                else:
                    continue
            count += 1
    return count


if __name__ == '__main__':
    stack = 'abababa'
    needle = 'baba'
    s = [[x] for x in stack]
    n = [[x] for x in needle]

    s = [['a'], ['b'], ['a'], ['b'], ['a'], ['b'], ['a']]
    n = [['b'], ['a'], ['b'], ['a']]
    assert matches(s, n) == 2
