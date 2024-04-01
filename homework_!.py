class Node: #item으로 value를 가지고 link를 가진다. link가 없을 경우, None을 입력한다.
    def __init__(self, item = None, link = None): #None -> item,link 값을 안주었을떄 오류발생하는 것 방지.
        self.item = item
        self.link = link


# 추가, 출력, 탐색, 길이, 중간 삽입, 삭제,
class Linkedlist:

    def __init__(self,item = None):
        self.root = None

    def append(self, item =None): #가장 뒤에 값을 추가하는 함수.
        if self.root == None: #처음부터 빈 연결리스트인 경우
           self.root = Node(item) #가장 처음 노드인 루트노드에 item값 할당 단. link는 None값이 그대로 유지된다.

        else:
            curNode = self.root #현재 노드는 처음노드로 설정.
            while curNode.link != None: #현재의 노드의 링크값이 None이 아닐때까지 실행.
                curNode = curNode.link #현재노드를 현재노드의 링크값으로 갱신 -> 다음노드로 이동.
            curNode.link = Node(item) #마지막노드의 링크값 None에서 뒤에 새로운 값을 추가하는 구문.

    def print(self):
        curNode = self.root #현재의 노드는 처음노드로 설정.
        while curNode.link != None: #현재의 노드의 링크값이 None이 아닐때까지 실행.
            print(curNode.item, end=''"->") #현재 노드의 아이템 값을 출력
            curNode = curNode.link #다음 노드로 이동
        print(curNode.item) #마지막 노드의 아이템을 따로 출력.

    def find(self, item):
        curNode = self.root #현재의 노드를 처음노드로 설정.
        num = 0 #초기 인덱스 값인 0을 정의
        if curNode.item == item: #찾는 아이템이 처음에 바로 나온 경우.
            return 0
        else:
            while curNode.link != None: #현재의 노드의 링크값이 None이 아닐때까지 실행.
                curNode = curNode.link
                num = num+1 #다음 노드로 이동 후 인덱스 값 1 증가.
                if curNode.item == item: # 이동하는 과정 중에 원하는 값 찾은 경우
                    return num #해당 인덱스 값을 출력.
            return -1 # 이동을 다 했는데도 해당 아이템이 나타나지 않은 경우 -1 출력
        #위에 return -1 구문을 while문 안에 넣는것을 주의해야한다.

    def listsize(self):
        num = 1 #사이즈는 인덱스 값이 아닌 길이이므로 초기값을 1로 설정.
        curNode = self.root
        while curNode.link != None:  # 마지막에서 2번째 노드의 링크.
            curNode = curNode.link # 다음노드로 이동. (마지막 노드로 이동한 것.)
            num = num + 1  # 다음노드로 이동 후 길이 1씩 증가.
        return num

    def insert(self, num, item ):
        if num == 0: #처음 노드에 삽입하는 경우.
            _tmp = self.root #기존의 처음 노드를 일단 다른곳에 저장.
            self.root = Node(item) #처음 노드에 삽입할 노드를 넣어줌.
            self.root.link = _tmp #처음 노드가 가르키는 링크가 기존 첫번째를 가르키도록 설정.

        else: #중간에 삽입하는 경우.
            curNode = self.root #처음 노드는 그대로.
            for i in range(num-1): #삽입을 원하는 위치 전까지 이동해줌
                curNode = curNode.link
            _tmp = curNode.link #삽입을 원하는 위치에 있는 노드를 따로 빼줌.
            newNode = Node(item) #삽입 원하는 노드를 만들어줌.
            curNode.link = newNode #삽입 전 노드의 링크가 새로운 노드를 가르키도록 설정.
            newNode.link = _tmp #삽입한 코드의 링크가 원래 있던 노드를 가르키도록 설정.

    def delete(self,item):
        #삭제하기 전에 삭제할 노드가 어디위치에 존재하는지 확인해야함.
        num = self.find(item)
        if num == -1: # 만약 삭제할 아이템이 존재하지 않으면 아무것도 삭제X
            return 0

        if num == 0: #처음 노드를 삭제할 경우
            self.root = self.root.link #처음 노드는 기존의 루트노드가 가르키던 노드이다.

        else: #처음 노드 삭제가 아닌경우.
            curNode = self.root #처음 노드부터 시작.
            for i in range(num-1): #삭제할 노드의 위치 그 전까지 이동.
                curNode = curNode.link
            curNode.link = curNode.link.link # 그 다음 노드는 지금 노드가 가르키는 노드(삭제할 노드)가 가르키는 노드
            #즉 삭제할 노드를 건너뛰는 코드이다.







fruits = Linkedlist()
fruits.append("사과")
fruits.append("앵두")
fruits.append("배")
fruits.append("포도")

fruits.print()
fruits.insert(2,"딸기")
fruits.print()
print(fruits.listsize())

item = input("삭제를 원하는 과일을 입력하세요: ")
fruits.delete(item)
fruits.print()