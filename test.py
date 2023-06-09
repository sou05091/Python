def dfs(graph, start_node):
    visited = set()  # 방문한 노드를 기록하기 위한 집합(set)
    stack = [start_node]  # 방문해야 할 노드를 스택에 저장

    while stack:
        node = stack.pop()  # 스택의 가장 위에 있는 노드를 가져옴

        if node not in visited:  # 방문한 적이 없는 경우에만 실행
            print(node)  # 현재 노드 출력
            visited.add(node)  # 현재 노드를 방문한 것으로 처리

            neighbors = graph[node]  # 현재 노드의 인접한 노드들을 가져옴
            for neighbor in neighbors:
                if neighbor not in visited:  # 인접한 노드 중에서 방문하지 않은 노드를 스택에 추가
                    stack.append(neighbor)
# 그래프를 인접 리스트로 표현
graph = {
    'A': ['C', 'B'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# 노드 'A'에서 시작하여 DFS 수행
dfs(graph, 'A')

