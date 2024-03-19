# Node Class: item으로 value를 가지고 link를 가진다. link가 없을 경우, None을 입력한다.
class Node:
    def __init__(self, item = None, link = None): # 객체가 생성될 때 자동으로 실행됨 None -> item,link 값을 안주었을떄 오류발생하는 것 방지.
        self.item = item
        self.link = link

a = Node('사과')
print(a)
print(a.item)
print(a.link)

class LinkedList:

    def __init__(self, item=None):
        self.root = None

    def append(self, item):
        if self.root == None:
            self.root = Node(item)
        else:
            curNode = self.root
            while curNode.link != None:
                curNode = curNode.link
            curNode.link = Node(item)

    def print(self):
        curNode = self.root
        while curNode.link != None:
            print(curNode.item, end="->")
            curNode = curNode.link
            print(curNode.item)

    def find(self, item):
        num = 1
        curNode = self.root
        while curNode.link != None:

            if curNode.item == item:
                print(curNode.link)
                print(num)
                break
            else:
                curNode = curNode.link
                num += 1

        curNode.link = Node(item)

    # 순서가 증가할수록 값을 1씩 증가. + 주소값도 출력

item = input("원하는 과일을 입력하세요: ")

fruits = LinkedList()
fruits.append("사과")
fruits.append("앵두")
fruits.append("배")
fruits.append("포도")

fruits.find(item)
