class Node:
    def __init__(self, coef=None, exp=None, link=None):
        self.coef = coef  # 다항식의 계수를 저장.
        self.exp = exp  # 다항식의 차수를 저장.
        self.link = link  # 다음 노드를 가르킴.

class Poly_linked:
    def __init__(self):
        self.root = None  # 다항식의 첫 번째 항 초기값 설정.

    # 다항식에 새로운 항을 삽입하는 메서드.
    def insert(self, coef, exp):
        # 새로운 노드를 생성.
        newNode = Node(coef, exp)

        # 다항식의 항을 차수에 따라 내림차순으로 삽입.
        if self.root is None or exp > self.root.exp:  # 새로운 항이 첫 번째 항이거나 다항식이 비어있는 경우
            newNode.link = self.root
            self.root = newNode
        else:
            curNode = self.root
            while curNode.link is not None and curNode.link.exp >= exp:
                curNode = curNode.link
            newNode.link = curNode.link
            curNode.link = newNode

    # 두 다항식의 합을 계산하는 클래스 메서드.
    @classmethod
    def add(cls, p, q):
        r = Poly_linked()  # 결과 다항식을 저장할 객체를 생성.
        curNode1 = p.root  # 첫 번째 다항식의 루트 노드.
        curNode2 = q.root  # 두 번째 다항식의 루트 노드.

        # 다항식의 각 항을 더하면서 결과 다항식을 생성.
        while curNode1 is not None and curNode2 is not None:
            if curNode1.exp > curNode2.exp:  # 첫 번째 다항식의 차수가 더 큰 경우
                r.insert(curNode1.coef, curNode1.exp)  # 결과 다항식에 첫 번째 다항식의 항을 삽입.
                curNode1 = curNode1.link  # 다음 링크로 이동.
            elif curNode1.exp < curNode2.exp:  # 두 번째 다항식의 차수가 더 큰 경우
                r.insert(curNode2.coef, curNode2.exp)  # 결과 다항식에 두 번째 다항식의 항을 삽입.
                curNode2 = curNode2.link  # 다음 링크로 이동.
            else:  # 첫 번째 다항식과 두 번째 다항식의 차수가 같은 경우
                r.insert(curNode1.coef + curNode2.coef, curNode1.exp)  # 결과 다항식에 합을 삽입.
                curNode1 = curNode1.link  # 다음 링크로 이동.
                curNode2 = curNode2.link  # 다음 링크로 이동.

        # 남은 항들을 결과 다항식에 추가.
        while curNode1 is not None:  # 첫 번째 다항식에 남은 항이 있는 경우
            r.insert(curNode1.coef, curNode1.exp)  # 결과 다항식에 해당 항을 삽입.
            curNode1 = curNode1.link  # 다음 항으로 이동.
        while curNode2 is not None:  # 두 번째 다항식에 남은 항이 있는 경우
            r.insert(curNode2.coef, curNode2.exp)  # 결과 다항식에 해당 항을 삽입.
            curNode2 = curNode2.link  # 다음 항으로 이동.

        return r

    # 다항식 출력 메서드
    def display(self):
        curNode = self.root  # 현재 노드를 다항식의 첫 번째 항으로 설정.
        while curNode is not None:  # 현재 노드가 None이 아닐 때까지 반복.
            print(curNode.coef, end="")  # 현재 항의 계수를 출력.
            if curNode.exp != 0:  # 현재 항의 차수가 0이 아닌 경우
                print("x^" + str(curNode.exp), end=" + ")  # "x^차수" 형식으로 출력.
            curNode = curNode.link  # 다음 노드로 이동.


# 다항식 p 생성: 4x^4 + 3x^3 + 3x^1
p = Poly_linked()
p.insert(4, 4)
p.insert(3, 3)
p.insert(3, 1)

# 다항식 q 생성: 3x^4 + 4x^2 + 2x^1 + 4x^0
q = Poly_linked()
q.insert(3, 4)
q.insert(4, 2)
q.insert(2, 1)
q.insert(4, 0)

# 다항식의 합 계산 및 출력
r = Poly_linked.add(p, q)
Poly_linked.display(r)