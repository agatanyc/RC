"""Write a function that takes a two strings representing times on a 24 hour clock.
 These are the time something was supposed to be done, and the time it was actually done 
 (you can assume each pair takes place in the same calendar day).
  Each time the function gets a pair, it should print the average lateness of all 
  events that it has received.

late("3:30", "4:00") # prints 0:30
late("14:20", "14:00") # prints 0:05 - the average of 30 minutes and -20 minutes
"""
COUNTER = 0
TOTAL_DIFF = 0
def diff_and_counter(planned, occured):
    counter = 0
    total_diff = 0
    def diff(planned, occured):
        """ (str, str) -> str"""
        # convert the string to a flaot
        p = float(planned.replace(':', '.'))
        o = float(occured.replace(':', '.'))
        return o - p
    counter += 1
    total_diff += diff(planned, occured)
    return (total_diff, counter)

planned = '3:30'
occured = '4:00'

COUNTER += diff_and_counter(planned, occured)[1]
TOTAL_DIFF += diff_and_counter(planned, occured)[0]

def late(planned, occured):
    ret = diff_and_counter(planned, occured)
    return ret[0] / ret[1]

print 'LATE: ', late("3:30", "4:00")
print 'LATE: ', late("14:20", "14:00")
#print 'LATE: ', late()



