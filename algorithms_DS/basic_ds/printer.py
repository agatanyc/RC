"""Study the behavior of the printing queue in a student lab."""
from queue import Queue

class Printer(object):
    """Track whether there is a current task."""
    def __init__(self, ppm):
        self.pagerate = float(ppm) # pages printed per minute - 5 or 10
        self.currentTask = None
        self.timeRemaining = 0     # seconds

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * (60.0/self.pagerate)

import random
class Task(object):
    """Represent single printing task."""
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21) # anywhere between 1 and 20

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        """Diferrence between now and when the task was created."""
        return currenttime - self.timestamp

def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds): # 3600 sec == 1h
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)


        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait = sum(waitingtimes) / len(waitingtimes)
    print "Average Wait %6.2f secs %3d tasks remaining."%(
            averageWait,printQueue.size())


def newPrintTask():
    """Print tasks arrive once every 180 seconds."""
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False

if __name__ == '__main__':

    print "Rate of 5 pages per minute:"
    for i in range(10):
        """Simulation run for a period of 60 minutes (3,600 seconds) using
        a page rate of five pages per minute.""" 
        simulation(3600, 5)

    print '___________________________'
    print "Rate of 10 pages per minute:"
    for i in range(10):
        """Ten pages per mnute."""
        simulation(3600,10)

