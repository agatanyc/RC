"""You go into a very small grocery store with a fixed amount of money,
wanting to spend as much of your budget as possible on a single item.
What will you be eating this week, and how much of it can you afford?

lifeskills(20.04, {'ketchup': 2.99, 'avocados': 0.99, 'milk': 3.25})
-> ('avocados', 20) # leaving 24 cents"""

from __future__ import division

def will_eat(xs):
    # xs is a tuple called `lifeskills` in the example above
    n = xs[0]
    food_items = xs[1]
    d = {}
    # map the item to the change potentialy received
    for k, v  in food_items. iteritems():
        d[k] = n % v
    # item and ths value that leaves us with min change
    min_value = min(d.itervalues())
    final_items = [k for k, v in d.iteritems() if v == min_value]
    final_item = final_items[0]
    return final_item, n // food_items[final_item] 

if __name__ == '__main__':
    xs = (20.04, {'ketchup': 2.99, 'avocados': 0.99, 'milk': 3.25})
    print will_eat(xs)

    assert will_eat(xs) == ('avocados', 20.0)

