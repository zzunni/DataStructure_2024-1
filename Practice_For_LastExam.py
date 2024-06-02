class BinaryTree:
    def __init__(self):
        # 트리의 초기화를 담당하는 생성자 메서드
        self.t = [None]  # 트리를 나타내는 배열. 인덱스 0은 사용하지 않으므로 None으로 초기화
        self.size = len(self.t)  # 트리의 현재 크기

    def append(self, item):
        # 트리에 새로운 요소를 추가하는 메서드
        self.t.append(item)  # 배열의 끝에 새로운 요소를 추가
        self.size += 1  # 트리의 크기를 1 증가

    def getChild(self, item):
        # 특정 요소의 자식을 반환하는 메서드
        idx = self.t.index(item)  # 주어진 요소의 인덱스를 찾음
        leftChildIdx = idx * 2  # 왼쪽 자식의 인덱스 계산
        rightChildIdx = leftChildIdx + 1  # 오른쪽 자식의 인덱스 계산
        if leftChildIdx >= self.size:
            # 왼쪽 자식의 인덱스가 트리의 크기보다 크거나 같으면 왼쪽 자식 없음
            leftChildIdx = None
            rightChildIdx = None  # 오른쪽 자식도 없음 (왼쪽 자식이 없으면 오른쪽 자식도 있을 수 없음)
        elif rightChildIdx >= self.size:
            # 오른쪽 자식의 인덱스가 트리의 크기보다 크거나 같으면 오른쪽 자식 없음
            rightChildIdx = None
        return self.t[leftChildIdx], self.t[rightChildIdx]  # 왼쪽 자식과 오른쪽 자식을 반환

    def getParent(self, item):
        # 특정 요소의 부모를 반환하는 메서드
        if item in self.t:
            idx = self.t.index(item)  # 주어진 요소의 인덱스를 찾음
            return self.t[idx // 2]  # 부모의 인덱스는 현재 인덱스의 절반 값
        else:
            # 주어진 요소가 트리에 없으면 경고 메시지 출력
            print("item not found")

tree = BinaryTree()  # 이진 트리 객체 생성
for i in range(12):
    # A부터 L까지의 알파벳을 트리에 추가
    tree.append(chr(65 + i))

# 'D'의 자식 노드를 출력
print(tree.getChild('D'))

# 'A'의 부모 노드를 출력
print(tree.getParent('A'))
