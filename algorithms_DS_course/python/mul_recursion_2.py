def cell_value(x, y):
    #if x ==1:
        #    return y
    if y == 1:
        return x
    else:
        if x > 1:
            return x + cell_value(x, y - 1)
        #if y > 1:
         #   return y + cell_value(x - 1, y)
    

print cell_value(2, 2)
print cell_value(6, 6)
            
