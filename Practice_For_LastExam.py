class Graph:
    def __init__(self, graph, start):
        self.graph = graph  # 그래프를 딕셔너리 형태로 저장
        self.start = start  # 시작 노드
        self.s = Stack()    # 스택 객체 생성
        self.visit = []     # 방문한 노드를 기록할 리스트

    def dfs(self):
        self.s.push(self.start)  # 시작 노드를 스택에 푸시
        while self.s.isEmpty() == False:  # 스택이 비어있지 않은 동안 반복
            curNode = self.s.pop()  # 스택에서 현재 노드를 팝
            if curNode not in self.visit:  # 현재 노드가 방문한 적이 없는 경우
                self.visit.append(curNode)  # 방문한 노드로 등록
                # 현재 노드의 이웃 노드 중 방문하지 않은 노드 집합을 스택에 푸시
                for node in sorted(list(set(self.graph[curNode]) - set(self.visit))):
                    self.s.push(node) # 방문하지 않은 노드를 찾아내 스택에 푸시. 이를 통해 DFS가 계속 진행
        return self.visit  # 방문한 노드 순서대로 반환

    def bfs(self):
        visit = [self.start]  # 시작 노드를 방문 목록에 추가
        for item in self.graph[self.start]:  # 시작 노드의 이웃 노드를 큐에 추가
            self.q.enQueue(item)

        while self.q.isEmpty() == False:  # 큐가 비어있지 않은 동안 반복
            item = self.q.deQueue()  # 큐에서 노드를 디큐
            if not item in visit:  # 노드가 방문하지 않은 노드라면
                for _item in self.graph[item]:
                    self.q.enQueue(_item)  # 노드의 이웃 노드를 큐에 추가
                visit.append(item)  # 방문 목록에 추가
        return visit
