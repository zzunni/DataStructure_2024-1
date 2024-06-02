class BNode:
    def __init__(self, item):
        # 노드의 초기화를 담당하는 생성자 메서드
        self.item = item  # 노드가 저장하는 값
        self.left = None  # 왼쪽 자식 노드를 가리키는 포인터
        self.right = None  # 오른쪽 자식 노드를 가리키는 포인터

    def setLeft(self, node):
        # 왼쪽 자식 노드를 설정하는 메서드
        self.left = node

    def setRight(self, node):
        # 오른쪽 자식 노드를 설정하는 메서드
        self.right = node

class BinaryTree:
    def __init__(self, root):
        # 트리의 초기화를 담당하는 생성자 메서드
        self.root = root  # 트리의 루트 노드

    def preOrder(self, n):
        # 전위 순회 메서드
        print(n.item, ' ', end=' ')  # 현재 노드를 먼저 방문
        if n.left:
            self.preOrder(n.left)  # 왼쪽 자식을 재귀적으로 방문
        if n.right:
            self.preOrder(n.right)  # 오른쪽 자식을 재귀적으로 방문

    def inOrder(self, n):
        # 중위 순회 메서드
        if n.left:
            self.inOrder(n.left)  # 왼쪽 자식을 먼저 재귀적으로 방문
        print(n.item, ' ', end=' ')  # 현재 노드를 방문
        if n.right:
            self.inOrder(n.right)  # 오른쪽 자식을 재귀적으로 방문

    def postOrder(self, n):
        # 후위 순회 메서드
        if n.left:
            self.postOrder(n.left)  # 왼쪽 자식을 먼저 재귀적으로 방문
        if n.right:
            self.postOrder(n.right)  # 오른쪽 자식을 재귀적으로 방문
        print(n.item, ' ', end=' ')  # 현재 노드를 마지막에 방문

# 노드들을 생성하고 각 노드에 값을 할당
a = BNode('A')
b = BNode('B')
c = BNode('C')
d = BNode('D')
e = BNode('E')
f = BNode('F')
g = BNode('G')
h = BNode('H')
i = BNode('I')
j = BNode('J')
k = BNode('K')

# 각 노드를 트리에 연결하여 구조를 형성
a.setLeft(b)
a.setRight(c)
b.setLeft(d)
b.setRight(e)
c.setLeft(f)
c.setRight(g)
d.setLeft(h)
e.setLeft(i)
e.setRight(j)
g.setRight(k)

# 트리를 생성하고 루트 노드를 A로 설정
bt = BinaryTree(a)

# 전위 순회를 실행하고 결과를 출력
bt.preOrder(a)
print()  # 결과를 구분하기 위해 줄 바꿈

# 중위 순회를 실행하고 결과를 출력
bt.inOrder(a)
print()  # 결과를 구분하기 위해 줄 바꿈

# 후위 순회를 실행하고 결과를 출력
bt.postOrder(a)
print()  # 결과를 구분하기 위해 줄 바꿈
