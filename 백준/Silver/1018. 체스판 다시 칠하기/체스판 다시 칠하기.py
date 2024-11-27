def min_repaint_to_chessboard(n, m, board):
    def count_repaints(x, y, first_color):
        """(x, y)에서 시작하는 8x8 체스판에서 다시 칠해야 하는 칸 수를 계산"""
        repaint_count1 = 0  # 첫 칸이 첫 색(first_color)인 경우
        repaint_count2 = 0  # 첫 칸이 반대 색인 경우
        
        for i in range(8):
            for j in range(8):
                current_color = first_color if (i + j) % 2 == 0 else ('B' if first_color == 'W' else 'W')
                if board[x + i][y + j] != current_color:
                    repaint_count1 += 1
                else:
                    repaint_count2 += 1
        return min(repaint_count1, repaint_count2)

    min_repaint = float('inf')  # 최소 다시 칠해야 하는 칸 수를 저장

    # 모든 8x8 체스판 부분을 검사
    for i in range(n - 7):
        for j in range(m - 7):
            min_repaint = min(min_repaint, count_repaints(i, j, 'B'), count_repaints(i, j, 'W'))
    
    return min_repaint


# 입력 처리
n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

# 결과 출력
print(min_repaint_to_chessboard(n, m, board))
