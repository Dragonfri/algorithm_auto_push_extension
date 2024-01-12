# 문제 : 바이러스
# 결과 :  / 속도: 40 / 메모리 : 31120
# 제출시각 : 24-01-12  20:19:11
import sys
def virus():
    input = sys.stdin.readline
​
    stack = []
    node = int(input())
    edge = int(input())
    edge_arr = [[] for _ in range(node + 1)]
​
    #node 갯수만큼 visited 배열을 False로 초기화
    visited = [False] * (node + 1)
    virus_cnt = 0
​
    # 이제 이걸 누가 누구랑 연결되어있는지 정리를 해야되는데...
    # a를 key 값으로 a: x, y, z
    # b를 key 값으로 b: q, w, e
    # 이런 식으로 정리가 된다면 1번이랑 연결된 얘들을 타고타고 들어가서 정답을 알아낼 수 있지 않을까?
    # a에서 x에 접속하고 x가 key값으로 누구랑 연결되어있는지 y는 누구랑... 쭉 타고들어가면 되니까
​
    #양방향 그래프임을 표현
    for _ in range(edge):
        a, b = map(int, input().split())
        edge_arr[a].append(b)
        edge_arr[b].append(a)
​
    # 1번 노드와 연결된 얘들을 돌면서 누구랑 연결 되어있는지 다 넣을거임
    stack.append(1)
    while stack:
        current = stack.pop()
        visited[current] = True
        for i in edge_arr[current]:
            if visited[i] is False:
                stack.append(i)
                visited[i] = True
                virus_cnt += 1
​
    print(virus_cnt)
​
virus()
​
