import pandas as pd
import tkinter as tk
from tkinter import messagebox

class Dijkstra:
    def __init__(self):
        self.graph = []
        self.nodes = set()

    def setEdge(self, a, b, w):
        self.graph.append((a, b, w))
        self.nodes.update([a, b])

    def _neighbor(self, curNode):
        neighbor = {}
        for node in self.graph:
            if node[0] == curNode:
                neighbor[node[1]] = node[2]
            elif node[1] == curNode:
                neighbor[node[0]] = node[2]
        return neighbor

    def _getWeight(self, n1, n2):
        for node in self.graph:
            if (node[0] == n1 and node[1] == n2) or (node[0] == n2 and node[1] == n1):
                return node[2]
        return None

    def _dicFilter(self, cost, nodes):
        import sys
        mini = sys.maxsize
        curNode = None
        for key, value in cost.items():
            if key in nodes and value[0] < mini:
                mini = value[0]
                curNode = key
        return curNode

    def getPath(self, start, end):
        import sys

        cost = {node: [sys.maxsize, None] for node in self.nodes}
        cost[start] = [0, start]
        visits = set()
        nodes = set(self.nodes)
        curNode = start

        while nodes:
            visits.add(curNode)
            nodes.remove(curNode)
            neighbors = self._neighbor(curNode)

            for node in neighbors:
                new_cost = cost[curNode][0] + self._getWeight(curNode, node)
                if new_cost < cost[node][0]:
                    cost[node][0] = new_cost
                    cost[node][1] = curNode

            curNode = self._dicFilter(cost, nodes)
            if curNode is None:
                break

        if cost[end][0] == sys.maxsize:
            raise ValueError("경로를 찾을 수 없습니다")

        path = [end]
        while end != start:
            path.append(cost[end][1])
            end = cost[end][1]

        return path[::-1], cost[path[0]][0]

# Subway.csv 파일 로드 (경로 수정)
subway_df = pd.read_csv(r'C:\Users\PC\Desktop\최예준 폴더\3학년 2학기\자료구조론\DataStructure_2024-1\Subway.csv', header=None)
subway_df.columns = ['StartStation', 'EndStation', 'Weight']

# Dijkstra 클래스 인스턴스 생성 및 그래프 구성
dijkstra = Dijkstra()

for _, row in subway_df.iterrows():
    dijkstra.setEdge(row['StartStation'], row['EndStation'], row['Weight'])

def calculate_path():
    start = start_entry.get()
    end = end_entry.get()
    try:
        path, cost = dijkstra.getPath(start, end)
        result = f"Path: {' -> '.join(path)}\nCost: {cost}"
    except ValueError as ve:
        result = str(ve)
    except Exception as e:
        result = str(e)
    messagebox.showinfo("Result", result)

# Tkinter 윈도우 생성
window = tk.Tk()
window.title("Dijkstra Path Finder")
window.geometry("400x200")

# 출발역 입력
tk.Label(window, text="Start Station:").grid(row=0, column=0, padx=10, pady=10)
start_entry = tk.Entry(window)
start_entry.grid(row=0, column=1, padx=10, pady=10)
start_entry.insert(0, '서울역(1)')  # 기본값 설정

# 도착역 입력
tk.Label(window, text="End Station:").grid(row=1, column=0, padx=10, pady=10)
end_entry = tk.Entry(window)
end_entry.grid(row=1, column=1, padx=10, pady=10)
end_entry.insert(0, '종로3가(1)')  # 기본값 설정

# 결과출력 버튼
tk.Button(window, text="Calculate Path", command=calculate_path).grid(row=2, columnspan=2, pady=20)

window.mainloop()
