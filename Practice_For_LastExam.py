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
   def levelOrder(self):
        # 루트 노드의 높이를 구한 다음 높이가 1부터 h까지 순차적으로 노드를 구한다.
        h = self.height(self.root)
        for i in range(1, h + 1): # 높이가 1, 2, ... , h 까지 순차적으로 프린트한다. 루트의 높이는 1이고, 바로 밑은 높이가 2다.
            self._levelOrder(self.root, i)
            print()

    # 특정 노드의 레벨에 해당하는 노드를 프린트한다.
    # 예: 루트에서 레벨 2를 프린트한다면 레벨을 한 단계 낮춰 루트 좌우로 이동한다.
    #     이후, 레벨 1이 되므로 루트의 좌, 우 노드가 프린트 된다.
    #     레벨 3을 프린트 한다면 레벨을 한 단계 낮춘 상태 즉 루트 바로 밑을 루트로 보고 재귀적으로 레벨 2를 수행하는 것이다.

    def _levelOrder(self, node, level):
        if node is None:
            return
        # 특정 노드의 level == 1일 때, 특정 노드 값을 인쇄한다.
        if level == 1:
            print(node.item, end = " ")
        # level > 1 이면 특정 노드의 좌, 우측으로 이동해서 레벨을 다운시켜 진행한다.
        elif level > 1:
            self._levelOrder(node.left, level - 1)
            self._levelOrder(node.right, level - 1)