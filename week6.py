import copy

class SparseMatrix:
  def __init__(self,m,n):
    self.s = [[m,n,0]] # 빈 matrix 생성
    self.m = m # 다른 곳에서도 m,n 값이 필요하기 때문에 세이브 해놓은것. 지역번수 m,n 을 광역변수로 변환해준것.
    self.n = n

  def append(self, i, j, val):
    self.s.append([i,j,val])
    self.s[0][2] += 1  #non zero element 수 증가시켜주는 것.

  def peek(self, ii, jj):
    for i in range(1, self.s[0][2]+1): #0번째는 해드이므로 탐색할 필요 없음. 따라서 1부터 탐색 시작.
      if self.s[i][0] == ii and self.s[i][1] == jj: #같은 위치의 행렬에서 찾았다는 조건.
        return self.s[i][2] # -> 벨류값 리턴해주는 것.
    return 0 #못찾은 경우 0을 리턴해줌.

  @classmethod
  def transpose(cls, x):
    xt = copy.deepcopy(x) #x랑 똑같은데 물리적으로는 다름.
    for _s in xt.s:
      _s[0], _s[1] = _s[1], _s[0] #파이썬만 가능한 문법.
    return xt

  @classmethod
  def add(cls, a, b):
    if a.m != b.m: #행렬 덧셈뺄셈 불가능한 경우.
      print("Error")
      return
    if a.n != b.n:
      print("Error")
      return

    # a = [[m, n, nonzero]]부터 시작이므로
    c = SparseMatrix(a.m, a.n)               # c행렬 생성.
    for i in range(1, a.s[0][2]+1):          #a행렬 b행렬 1:1 대응시키면서 찾는것.
      _tmp = a.peek(a.s[i][0], a.s[i][1]) + b.peek(a.s[i][0], a.s[i][1]) #같은 위치의 값 더해줌.
      if _tmp != 0:                          #더한 값이 0이 아닐때 즉, value값을 가질 때
        c.append(a.s[i][0], a.s[i][1], _tmp) #새로운 c 행렬에 value값을 append 해준다.

    for i in range(1, b.s[0][2] + 1):  # a행렬 b행렬 1:1 대응시키면서 찾는것.
      _tmp = a.peek(b.s[i][0], b.s[i][1]) + b.peek(b.s[i][0], b.s[i][1])  # 같은 위치의 값 더해줌.
      if _tmp != 0 and c.peek(b.s[i][0], b.s[i][1]) == 0:  # 더한 값이 0이 아닐때 즉, value값을 가질 때, 그리고 a에서 더했을때도 0이었을때.(중복계산 방지)
        c.append(b.s[i][0], b.s[i][1], _tmp)  # 새로운 c 행렬에 value값을 append 해준다.

    return c



a = SparseMatrix(4,3)
a.append(0,0,1)
a.append(0,2,2)
a.append(1,2,3)
a.append(1,0,4)
a.append(1,1,6)
a.append(2,2,7)
a.append(3,1,3)

b = SparseMatrix(4,3)
b.append(0,0,1)
b.append(0,2,-2)
b.append(1,0,4)
b.append(1,1,6)
b.append(2,2,7)
b.append(3,1,3)
b.append(3,0,1)

at = SparseMatrix.transpose(a)
c = SparseMatrix.add(a, b)
print(c)