from collections import deque
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # 음
        # 그냥 클릭 위치를 잡고
        # 만약 방문을 안했고
        # E인 경우에는 방문표시 and 큐에 넣기
        # M인 경우에는 지뢰수를 센 다음에 값 바꾸기
        # flag를 설정해서 mine이 있으면 False가 되도록

        def bfs(q, visited):
            next_yx = [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]

            while q:
                current_y, current_x = q.popleft()
                if board[current_y][current_x] == "M":
                    board[current_y][current_x] = "X"
                    return

                mine_cnt = 0
                cnt = 0

                for y,x in next_yx:
                    next_y = current_y + y
                    next_x = current_x + x

                    if 0 <= next_y < len(board) and 0 <= next_x < len(board[0]):
                        if (next_y, next_x) not in visited: #뭐인진 모름
                            if board[next_y][next_x] == "M":
                                mine_cnt += 1
                            elif board[next_y][next_x] == "E":
                                cnt += 1
                                q.append((next_y, next_x))
                                visited.add((next_y, next_x))
                if mine_cnt:
                    board[current_y][current_x] = str(mine_cnt)
                    for _ in range(cnt):
                        visited.remove(q.pop())
                else:
                    board[current_y][current_x] = "B"
        q = deque()
        q.append((click[0], click[1]))
        visited = set()
        visited.add((click[0], click[1]))
        bfs(q, visited)
        return board