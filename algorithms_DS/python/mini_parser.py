#!/usr/bin/env python2

"""
Given a nested list of integers represented as a string, implement a parser
to deserialize it.  Each element is either an integer, or a list -- whose
elements may also bei integers or other lists.
"""

indent = ''

class NestedInteger(object):
    """
    This is the interface that allows for creating nested lists.
    You should not implement it, or speculate about its implementation
    """

    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        pass

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        pass

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        pass

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        pass

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        pass

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        pass

class Solution(object):

    def _split_after_closer(self, s):
        depth = 0
        i = 0
        while i < len(s):
            if s[i] == '[':
                depth += 1
            elif s[i] == ']':
                depth -= 1
                if depth == 0:
                    return s[:i], s[i:]
            i += 1
        return s, ''

    def _deserialize_list_item(self, s):

        # find the end of the element
        # take the substring up to the end of the element
        # deserialize that substring
        # return the result

        assert s    # Don't accept empty strings.

        # If the item is a list, parse through the closing ']'
        if s[0] == '[':
            head, tail = self._split_after_closer(s)
            print "HEAD: '{}'".format(head), "TAIL: '{}'".format(tail)
            return self.deserialize(head), tail

        # Else, the item is an int.
        end = 0
        while end < len(s) and s[end] not in ",]":
            end += 1
        return self.deserialize(s[:end]), s[end:]

    def deserialize(self, s, index=0):
        """
        :type s: str
        :rtype: NestedInteger
        """

        global indent

        print indent, "DESERIALIZING:", s

        # If the string is empty:
        #   Return an empty NestedInteger.
        # Else if the string is an int:
        #   Parse, wrap, and return it.
        # Else:
        #   Initialize an empty result object.
        #   Add each (top-level) item in the "list" to the result.
        #   Return the result.

        if not s:
            print indent, "empty"
            return NestedInteger()

        try:
            print indent, int(s)
            return NestedInteger(int(s))
        except:
            pass

        r = NestedInteger()
        indent += '    '
        assert s[0] == '['
        while len(s) > 0 and s[0] != ']':
            print indent + "(looking at):", s
            x, s = self._deserialize_list_item(s[1:])
            r.add(x)
        indent = indent[:-4]
        return r

if __name__ == '__main__':
    sol = Solution()

    for s in ["", "42","[123,456]", "[123,[456]]", "[123,[456,789]]"]:
        print "\nPARSING: '{}'".format(s)
        sol.deserialize(s)
