class Node:
    def __init__(self, coef=None, exp=None, link=None):
        self.coef = coef  # 다항식의 계수를 저장합니다.
        self.exp = exp  # 다항식의 차수를 저장합니다.
        self.link = link  # 다음 노드를 가리킵니다.


class Poly_linked:
    def __init__(self):
        self.root = None  # 다항식의 첫 번째 항을 가리킵니다.

    def insert(self, coef, exp):
        # 새로운 노드를 생성합니다.
        newNode = Node(coef, exp)

        # 다항식의 항을 차수에 따라 내림차순으로 삽입합니다.
        if self.root == None or exp > self.root.exp:  # 새로운 항이 첫 번째 항이거나 다항식이 비어있는 경우
            newNode.link = self.root
            self.root = newNode
        else:
            curNode = self.root
            while curNode.link != None and curNode.link.exp >= exp:
                curNode = curNode.link
            newNode.link = curNode.link
            curNode.link = newNode

    @classmethod
    def add(cls, p, q):
        r = Poly_linked()  # 결과 다항식을 저장할 객체를 생성합니다.
        curNode1 = p.root  # 첫 번째 다항식의 루트 노드를 가져옵니다.
        curNode2 = q.root  # 두 번째 다항식의 루트 노드를 가져옵니다.

        # 다항식의 각 항을 더하면서 결과 다항식을 생성합니다.
        while curNode1 is not None and curNode2 is not None:
            if curNode1.exp > curNode2.exp:
                r.insert(curNode1.coef, curNode1.exp)
                curNode1 = curNode1.link
            elif curNode1.exp < curNode2.exp:
                r.insert(curNode2.coef, curNode2.exp)
                curNode2 = curNode2.link
            else:  # 차수가 같은 경우
                r.insert(curNode1.coef + curNode2.coef, curNode1.exp)
                curNode1 = curNode1.link
                curNode2 = curNode2.link

        # 남은 항들을 결과 다항식에 추가합니다.
        while curNode1 is not None:
            r.insert(curNode1.coef, curNode1.exp)
            curNode1 = curNode1.link
        while curNode2 is not None:
            r.insert(curNode2.coef, curNode2.exp)
            curNode2 = curNode2.link

        return r


# 다항식 p 생성: 4x^4 + 3x^2 + 3x^1
p = Poly_linked()
p.insert(6, 5)
p.insert(4, 3)
p.insert(4, 1)
p.insert(8,0)

# 다항식 q 생성: 3x^3 + 4x^2 + 2x^1 + 1x^0
q = Poly_linked()
q.insert(4, 3)
q.insert(5, 2)
q.insert(3, 1)
q.insert(2, 0)
q.insert(4,4)

# 다항식의 합 계산 및 출력
r = Poly_linked.add(p, q)
curNode = r.root
while curNode is not None:
    print(curNode.coef, end="")
    if curNode.exp != 0:
        print("x^" + str(curNode.exp), end=" + ")
    curNode = curNode.link
