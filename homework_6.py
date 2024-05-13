import copy
import numpy as np

class Queue:
    def __init__(self):
        self.q = []
    def isEmpty(self):
        return len(self.q) == 0
    def enQueue(self, item):
        self.q.append(item)
    def deQueue(self):
        if self.isEmpty() == True:
            return None
        else:
            return self.q.pop(0)
    def peek(self):
        return self.q[0]

    def size(self):
        return len(self.q)

class Cust:
    def __init__(self, aTime):
        self.arriveTime = aTime
        self.orderTime = 0
        self.outTime = 0

class Shop:
    def __init__(self):
        self.q = Queue()

    def size(self):
        return self.q.size()

    def enCust(self, c):
        self.q.enQueue(c)

    def outCust(self, curTime):
        while self.size() > 0 and self.q.peek().outTime < curTime:
            self.q.deQueue()

    def getLast(self):
        return self.q.q[-1] if self.size() > 0 else None

curTime = 0
s = Shop()
while curTime < 14 * 60:
    if 240 < curTime < 300:
        curTime += np.random.exponential(0.5) # 단일 값 반환
    else:
        curTime += np.random.exponential(1) # 단일 값 반환
    s.outCust(curTime)
    c = Cust(curTime)
    c = copy.deepcopy(c)
    if s.size() == 0:
        c.orderTime = c.arriveTime
    else:
        c.orderTime = s.getLast().outTime
    c.outTime = c.orderTime + np.random.normal(1, 0.2) # 단일 값 반환
    s.enCust(c)
    print(c.arriveTime, c.orderTime, c.outTime, s.size())
