def new_char(c,s):
    result = []
    for i in range(len(s)+1):
        temp = list(s)
        temp.insert(i,c)
        result.append(''.join(temp))
    return result

def rec_p(s):
    if len(s) == 2:
        return [s, s[::-1]]

    result = []
    for c in s:
        for permutation in rec_p(s.replace(c,'')):
            result.append(c + permutation)

    return result

print
print(rec_p('abc'))

