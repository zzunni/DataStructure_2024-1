# Node Class: item으로 value를 가지고 link를 가진다. link가 없을 경우, None을 입력한다.
class Node:
    def __init__(self, item = None, link = None): # 객체가 생성될 때 자동으로 실행됨 None -> item,link 값을 안주었을떄 오류발생하는 것 방지.
        self.item = item
        self.link = link


class LinkedList:

  def __init__(self, item = None):
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

  def listSize(self):
    k = 1
    curNode = self.root
    while curNode.link != None:
      curNode = curNode.link
      k += 1
    return k

  def find(self, item):
    curNode = self.root
    k = 0
    if curNode.item == item:
      return 0
    else:
      while curNode.link != None:
        curNode = curNode.link
        k += 1
        if curNode.item == item:
          return k
      return -1

    #내가 만든 find 함수
  # def find(self, item):
  #   num = 1
  #   curNode = self.root
  #   while curNode.link != None:
  #
  #     if curNode.item == item:
  #       print(curNode.link)
  #       print(num)
  #       break
  #     else:
  #       curNode = curNode.link
  #       num += 1
  #
  #   curNode.link = Node(item)

  def insert(self, k, item):

    if k == 0:
      _tmp = self.root
      self.root = Node(item)
      self.root.link = _tmp
    else:
      curNode = self.root
      for i in range(k-1):
        curNode = curNode.link
      _tmp = curNode.link
      newNode = Node(item)
      curNode.link = newNode
      newNode.link = _tmp


  def delete(self,item):
    k = self.find(item)
    if k == 0: #첫번째 노드를 삭제할 경우의 코드.
      self.root = self.root.link
    else:
      curNode = self.root
      for i in range(k-1):
        curNode = curNode.link
        #print(curNode,item) 돌다리도 두드리고 건너는 코드.
      curNode.link = curNode.link.link


  # 내가 만든 delete 함수인데 오류가 존재함.
  # def delete(self,item):
  #   k = fruits.find(item) #원하는 아이템이 몇번째 노드에 있는지 찾는 함수.
  #   curNode = self.root
  #
  #   for i in range(k): #k-1번째 노드까지 이동.
  #     curNode = curNode.link
  #
  #   if curNode.link.link == None:
  #     curNode.link = None
  #   else:
  #     curNode.link = curNode.link.link

fruits = LinkedList()
fruits.append("사과")
fruits.append("앵두")
fruits.append("배")
fruits.append("포도")

item = input("삭제를 원하는 과일을 입력하세요: ")
fruits.delete(item)

fruits.print()
# fruits.insert(2,"딸기")
# fruits.listSize()