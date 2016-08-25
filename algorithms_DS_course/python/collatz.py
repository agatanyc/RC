def calculate_next(n):
    count  = 1
    if n % 2 == 0:
        j = n / 2
        count += 1
    else: 
        j  = n * 3 + 1
        count += 1
    while j > 1:
        if j % 2 == 0:
            j = j / 2
            count += 1
        else:
            j = j * 3 + 1
            count += 1
    return count 

def largest(upto):
    largest = 0
    count = 0
    for x in range(upto):
        if calculate_next(x) > count:
            count = calculate_next(x)
            largest = x
    return largest


print largest(100)





