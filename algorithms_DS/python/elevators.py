"""Write a function that models the elevators in a building.
It will take 2 arguments:

* a list of numbers representing the floor each elevator starts on
* a list of (number, boolean) pairs representing elevator moves (so (3, True)
would mean to move elevator #3 up one floor; False means down)
Return a list representing the ending position of each elevator.

elevators([0, 0, 0], [(0, True), (2, False), (0, True), (1, True), (0, False)]
-> [1, 1, -1]
"""

def elevators(xs, ys):
    for y in ys:  #e.g. (0, True)
        if y[1] == True:
            index = y[0] # indicates which elevator moves
            xs[index] += 1
        else:
            index = y[0] # indicates which elevator moves
            xs[index] -= 1
    return xs



if __name__ == '__main__':
    xs = [0, 0, 0]
    ys = [(0, True), (2, False), (0, True), (1, True), (0, False)]
    
    assert elevators(xs, ys) == [1, 1, -1]

