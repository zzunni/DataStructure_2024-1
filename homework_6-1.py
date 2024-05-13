import copy
import numpy as np

class Queue:
    def __init__(self):
        self.q = []  # 큐를 나타내는 리스트 초기화

    def isEmpty(self):
        return len(self.q) == 0  # 큐가 비어 있는지 여부를 반환

    def enQueue(self, item):
        self.q.append(item)  # 큐에 아이템 추가

    def deQueue(self):
        if self.isEmpty():  # 큐가 비어 있는 경우
            return None
        else:
            return self.q.pop(0)  # 큐에서 아이템 제거하고 반환

    def peek(self):
        return self.q[0]  # 큐의 첫 번째 아이템 반환

    def size(self):
        return len(self.q)  # 큐의 길이 반환

class Cust:
    def __init__(self, aTime):
        self.arriveTime = aTime  # 고객의 도착 시간 초기화
        self.orderTime = 0  # 주문 시간 초기화
        self.outTime = 0  # 퇴장 시간 초기화

class Shop:
    def __init__(self, num_queues):
        self.queues = [Queue() for _ in range(num_queues)]  # 주어진 개수만큼 큐 생성
        self.num_queues = num_queues  # 큐의 개수 저장

    def enCust(self, c):
        # 가장 작은 큐를 찾아서 고객 추가
        min_queue = min(self.queues, key=lambda q: q.size())
        min_queue.enQueue(c)

    def outCust(self, curTime):
        # 각 큐에서 퇴장한 고객 제거
        for queue in self.queues:
            while queue.size() > 0 and queue.peek().outTime < curTime:
                queue.deQueue()

    def getLast(self):
        # 각 큐의 마지막 아이템 반환
        return [queue.q[-1] if queue.size() > 0 else None for queue in self.queues]

# 상점 초기화
s = Shop(3)  # 3개의 큐를 가진 상점

curTime = 0
while curTime < 14 * 60:  # 14시간 동안 반복
    # 도착 시간 계산
    if 240 < curTime < 300:
        curTime += np.random.exponential(0.5)  # 주어진 시간 간격으로 도착 시간 설정
    else:
        curTime += np.random.exponential(1)  # 주어진 시간 간격으로 도착 시간 설정

    # 이탈한 고객 처리
    s.outCust(curTime)

    # 새로운 고객 생성
    c = Cust(curTime)
    c = copy.deepcopy(c)

    # 주문 시간 설정
    if all(queue.size() == 0 for queue in s.queues):
        c.orderTime = c.arriveTime  # 모든 큐가 비어있는 경우
    else:
        last_times = s.getLast()
        min_last_time = min((last_time.outTime for last_time in last_times if last_time is not None), default=None)
        c.orderTime = min_last_time  # 마지막으로 주문한 고객의 주문 시간을 기준으로 설정

    # 퇴장 시간 설정
    c.outTime = c.orderTime + np.random.normal(1, 0.2)  # 주어진 평균과 표준편차로 퇴장 시간 설정

    # 가장 작은 큐에 고객 추가
    s.enCust(c)

    # 현재 시간과 큐의 상태 출력
    print(f"{c.arriveTime}, {c.orderTime}, {c.outTime}, {s.num_queues}")
