"""
def break(xs):
    for x in xs:
        if x == 5:
            break
        print x

xs = [1, 2, 3, 4, 5, 6, 7, 8]
break(xs)
"""


# Function to illustrate break in loop
def breakTest(arr):
    for i in arr:
        if i == 5:
            break
        print i,
    print


arr = [1, 2, 3, 4, 5, 6 ,7]
breakTest(arr)

# Function to illustrate continue in loop
def continueTest(arr):
    for i in arr:
        if i == 5:
            continue
        print i,
 
arr = [1, 2, 3, 4, 5, 6 ,7]
continueTest(arr)
