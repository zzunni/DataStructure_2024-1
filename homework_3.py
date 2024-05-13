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
  def multiply(cls, a, b):
    if a.n != b.m: #행렬 곱셈이 불가능한 경우.
      print("Error")
      return
    else:
      c = SparseMatrix(a.m, b.n)
      for i in range(1, a.m + 1):    #a행렬 b행렬 1:1 대응시키면서 찾는것.
        for j in range(1, b.n + 1):
          sum = 0
          for k in range(1, a.n + 1):    # 행렬 a의 각 열 또는 행렬 b의 각 행 요소에 대해
            sum += a.peek(i, k) * b.peek(k, j) # 행렬 곱셈의 핵심: 각 요소의 곱을 누적하여 합을 계산
          if sum != 0:     # 계산된 합이 0이 아니면 결과 행렬에 추가
            c.append(i,j,sum)

      return c

a = SparseMatrix(3,3)
a.append(1,1,1.)
a.append(2,3,2.)
a.append(3,2,3.)

b = SparseMatrix(3,3)
b.append(1,1,4.)
b.append(1,2,1.)
b.append(2,1,1.)
b.append(3,1,-1.)
b.append(3,2,1.)
b.append(2,3,-2.)

c = SparseMatrix.multiply(a, b)
for row in c.s:
    print(row)