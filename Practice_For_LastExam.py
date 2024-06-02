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
l = BNode('L')

# 각 노드를 트리에 연결하여 구조를 형성
a.setLeft(b)  # A의 왼쪽 자식으로 B를 설정
a.setRight(c)  # A의 오른쪽 자식으로 C를 설정
b.setLeft(d)  # B의 왼쪽 자식으로 D를 설정
b.setRight(e)  # B의 오른쪽 자식으로 E를 설정
c.setLeft(f)  # C의 왼쪽 자식으로 F를 설정
c.setRight(g)  # C의 오른쪽 자식으로 G를 설정
d.setLeft(h)  # D의 왼쪽 자식으로 H를 설정
d.setRight(i)  # D의 오른쪽 자식으로 I를 설정
e.setLeft(j)  # E의 왼쪽 자식으로 J를 설정
e.setRight(k)  # E의 오른쪽 자식으로 K를 설정
f.setLeft(l)  # F의 왼쪽 자식으로 L을 설정

# 트리를 생성하고 루트 노드를 A로 설정
t = BinaryTree(a)
