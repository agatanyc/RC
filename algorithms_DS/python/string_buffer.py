"""Convert list of strings to a string w/o creating new strings as we loop
through the list."""

import sys

path = '/Users/agata/dev/RC/algorithms_DS/basic_ds/'
sys.path.append(path)
from node import Node

def convert(xs):
     string_buffer = []
     for x in xs:
         string_buffer.append(x)
     return ''.join(string_buffer)

def convert_2(xs):
    str_buffer = Node(xs[0])
    head = str_buffer
    for i in range(len(xs) - 1):
        str_buffer.set_next(Node(xs[i + 1]))
        str_buffer = str_buffer.get_next()
    return head

if __name__ == '__main__':
    xs = ['r', 'a', 'c', 'h', 'e', 'l']
    node = convert_2(xs)
    while node:
        print node.get_data()
        node = node.get_next()
   
