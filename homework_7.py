class BinaryTree:
    def __init__(self):
        # 이진 트리의 노드를 저장할 리스트
        self.t = [None]
        # 트리의 크기
        self.size = len(self.t)

    def append(self, item):
        # 새로운 노드를 리스트에 추가
        self.t.append(item)
        # 트리 크기 증가
        self.size += 1

    def getChild(self, item):
        # 부모 노드의 인덱스 찾기
        idx = self.t.index(item)
        # 좌우 자식 노드의 인덱스 계산
        leftChildIdx = idx * 2
        rightChildIdx = leftChildIdx + 1
        # 좌우 자식 노드의 인덱스가 트리 크기보다 크면 해당 자식 노드가 없음
        if leftChildIdx >= self.size:
            leftChildIdx = None
            rightChildIdx = None
        elif rightChildIdx >= self.size:
            rightChildIdx = None
        # 좌우 자식 노드 반환
        return self.t[leftChildIdx], self.t[rightChildIdx]

    def getParent(self, item):
        # 노드가 리스트에 있는지 확인
        if item in self.t:
            # 노드의 인덱스 찾기
            idx = self.t.index(item)
            # 부모 노드의 인덱스 계산
            return self.t[idx // 2]
        else:
            # 노드가 리스트에 없으면 메시지 출력
            print("item not found")

    def calculateDistance(self, disease1, disease2):
        # 두 질병 사이의 경로 찾기
        path1 = self.findPath(disease1)
        path2 = self.findPath(disease2)

        # 두 경로 중 가장 가까운 공통 조상 찾기
        ancestor = None
        for node in path1:
            if node in path2:
                ancestor = node
                break

        # 두 노드 간의 거리 계산
        distance1 = path1.index(ancestor)
        distance2 = path2.index(ancestor)
        total_distance = distance1 + distance2

        # 결과 출력
        print(f"The distance between {disease1} and {disease2} is {total_distance}/3")

    def findPath(self, item):
        # 노드에서 루트까지의 경로 찾기
        path = []
        current_item = item
        while current_item != self.t[1]:
            parent = self.getParent(current_item)
            path.append(parent)
            current_item = parent
        # 경로 반환
        return path


# 이진 트리 생성
tree = BinaryTree()

# 노드 추가
tree.append("호흡기병")
tree.append("소화기병")
tree.append("호흡기감염")
tree.append("폐질환")
tree.append("위질환")
tree.append("결장질환")
tree.append("독감")
tree.append("기관지염")
tree.append("폐부종")
tree.append("폐색전증")
tree.append("위궤양")
tree.append("위암")
tree.append("대장염")
tree.append("대장암")

# 거리 계산
tree.calculateDistance("대장염", "대장암")
tree.calculateDistance("대장염", "위궤양")
tree.calculateDistance("대장염", "독감")
