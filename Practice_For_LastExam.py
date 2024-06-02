class MinHeap:
    def __init__(self):
        self.x = [None]  # 힙을 나타내는 배열 초기화. 첫 번째 요소를 None으로 설정하여 인덱스 계산을 간단하게 합니다.

    def _exchange(self, i, j):
        # 두 인덱스 i와 j의 값을 비교하고, self.x[i]가 self.x[j]보다 크면 두 값을 교환합니다.
        if self.x[i] > self.x[j]:
            self.x[i], self.x[j] = self.x[j], self.x[i]

    def push(self, item):
        self.x.append(item)  # 새로운 요소를 배열의 마지막에 추가합니다.
        cIndex = len(self.x) - 1  # 새로운 요소의 인덱스
        pIndex = cIndex // 2  # 부모 요소의 인덱스
        # 부모 인덱스가 1 이상인 동안 루프를 돌면서 힙 속성을 유지합니다.
        while pIndex >= 1:
            self._exchange(pIndex, cIndex)  # 필요시 부모와 자식을 교환합니다.
            cIndex = pIndex  # 자식 인덱스를 부모 인덱스로 업데이트합니다.
            pIndex = cIndex // 2  # 부모 인덱스를 재계산합니다.

    def pop(self):
        item = self.x[1]  # 힙의 루트 요소(최소값)를 제거합니다.
        n = len(self.x) - 1  # 마지막 요소의 인덱스
        self.x[1], self.x[n] = self.x[n], self.x[1]  # 루트 요소와 마지막 요소를 교환합니다.
        self.x = self.x[:-1]  # 마지막 요소를 제거합니다.
        self.heapify()  # 힙 속성을 유지하도록 재정렬합니다.
        return item  # 제거된 루트 요소를 반환합니다.

    def _child(self, pIndex):
        n = len(self.x)  # 현재 힙의 크기
        leftIndex = pIndex * 2  # 왼쪽 자식 인덱스
        rightIndex = pIndex * 2 + 1  # 오른쪽 자식 인덱스
        if rightIndex <= n - 1:
            return leftIndex, rightIndex  # 두 자식이 모두 있는 경우
        elif leftIndex == n - 1:
            return leftIndex, None  # 왼쪽 자식만 있는 경우
        else:
            return None, None  # 자식이 없는 경우

    def heapify(self):
        # 힙 속성을 유지하도록 재정렬하는 메서드입니다.
        pIndex = 1  # 루트 노드의 인덱스
        while pIndex < len(self.x):
            left, right = self._child(pIndex)  # 현재 노드의 자식 노드를 가져옵니다.
            if left != None and right == None:
                self._exchange(pIndex, left)  # 왼쪽 자식만 있는 경우, 필요시 교환합니다.
            elif left != None and right != None:
                if self.x[left] < self.x[right]:
                    self._exchange(pIndex, left)  # 왼쪽 자식이 더 작은 경우, 필요시 교환합니다.
                else:
                    self._exchange(pIndex, right)  # 오른쪽 자식이 더 작은 경우, 필요시 교환합니다.
            pIndex += 1  # 다음 노드로 이동합니다.

    def print(self):
        print(self.x)  # 현재 힙 배열을 출력합니다.

h = MinHeap()
for i in range(1, 9):
    h.push(i)  # 1부터 8까지의 숫자를 힙에 추가합니다.
print(h.x)  # 힙의 배열을 출력합니다.
for i in range(8):
    print(h.pop())  # 힙에서 요소를 하나씩 제거하여 출력합니다. 이 과정은 힙 정렬을 수행합니다.
