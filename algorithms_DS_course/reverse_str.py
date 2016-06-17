from stack import Stack

def reverse(string):
    s = Stack()
    rev = []
    for c in string:
        s.push(c)

    while not s.isEmpty():
        rev.append(s.pop())
    return "".join(rev)


string = 'agata'
assert reverse(string) == 'ataga'

