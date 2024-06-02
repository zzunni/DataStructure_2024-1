class MaxHeap:
    def __init__(self):
        # 힙을 나타내는 리스트를 초기화합니다. 첫 번째 요소는 사용하지 않으므로 None으로 설정합니다.
        self.x = [None]

    def _exchange(self, i, j):
        # 히든 메서드로, x[i]가 x[j]보다 작을 경우 두 값을 교환합니다.
        if self.x[i] < self.x[j]:
            self.x[i], self.x[j] = self.x[j], self.x[i]

    def push(self, item):
        # 힙에 새로운 요소를 추가하는 메서드입니다.
        self.x.append(item)  # 새로운 요소를 리스트의 마지막에 추가합니다.
        cIndex = len(self.x) - 1  # 새로 추가된 요소의 인덱스를 가져옵니다.
        pIndex = cIndex // 2  # 부모 노드의 인덱스를 계산합니다.
        while pIndex >= 1: # 부모 노드의 인덱스가 1 이상일 때까지 반복
            self._exchange(pIndex, cIndex)  # 부모와 자식의 위치를 교환하여 최대 힙 속성을 유지합니다.
            cIndex = pIndex
            pIndex = cIndex // 2

    def pop(self):
        # 힙에서 최대 값을 제거하고 반환하는 메서드입니다.
        item = self.x[1]  # 루트 요소(최대값)를 저장합니다.
        n = len(self.x) - 1  # 마지막 요소의 인덱스를 계산합니다.
        self.x[1], self.x[n] = self.x[n], self.x[1]  # 루트 요소와 마지막 요소를 교환합니다.
        self.x = self.x[:-1]  # 마지막 요소를 제거합니다.
        self.heapify()  # 최대 힙 속성을 유지하기 위해 힙을 재정렬합니다.
        return item

    def _child(self, pIndex):
        # 부모 노드의 인덱스를 입력받아 자식 노드의 인덱스를 반환하는 히든 메서드입니다.
        n = len(self.x) # 리스트에 있는 요소의 개수
        leftIndex = pIndex * 2  # 왼쪽 자식의 인덱스를 계산합니다.
        rightIndex = pIndex * 2 + 1  # 오른쪽 자식의 인덱스를 계산합니다.
        if rightIndex <= n - 1:
            return leftIndex, rightIndex  # 두 자식이 모두 있는 경우
        elif leftIndex == n - 1:
            return leftIndex, None  # 왼쪽 자식만 있는 경우
        else:
            return None, None  # 자식이 없는 경우

    def heapify(self):
        # 힙 속성을 유지하도록 재정렬하는 메서드입니다.
        pIndex = 1  # 시작 인덱스는 루트 노드의 인덱스입니다.
        lastIndex = len(self.x) - 1  # 마지막 인덱스를 계산합니다.
        while pIndex < len(self.x):  # 루트부터 마지막 노드까지 반복합니다.
            left, right = self._child(pIndex)  # 현재 노드의 자식 노드 인덱스를 가져옵니다.
            if left != None and right == None:
                self._exchange(pIndex, left)  # 왼쪽 자식만 있는 경우
            elif left != None and right != None:
                if self.x[left] < self.x[right]:
                    self._exchange(pIndex, right)  # 오른쪽 자식이 더 큰 경우
                else:
                    self._exchange(pIndex, left)  # 왼쪽 자식이 더 큰 경우
            pIndex += 1  # 다음 노드로 이동합니다.

    def print(self):
        # 힙을 출력하는 메서드입니다.
        print(self.x)
