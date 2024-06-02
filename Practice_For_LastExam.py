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

    def height(self, n):
        # 트리의 높이를 계산하는 메서드
        if n is None:
            return 0  # 터미널 노드를 만나면 0을 리턴
        else:
            lheight = self.height(n.left)  # 왼쪽 서브트리의 높이 계산
            rheight = self.height(n.right)  # 오른쪽 서브트리의 높이 계산
            # 왼쪽과 오른쪽 서브트리 중 더 큰 높이에 1을 더한 값이 현재 노드의 높이
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1
