class EightQueens:

    def __init__(self, size: int = 8):
        self.size = size
        self.queens = [-1]*size

    def is_safe(self, row: int, col: int) -> bool:
        #检查在当前棋盘状态下，在 (row, col) 放置皇后是否安全
        for r in range(row):
            if self.queens[r] == col or abs(col - self.queens[r]) == row - r:
                return False

        return True


    def place_queen(self, row: int, col: int) -> None:
        #在指定位置放置皇后（更新棋盘状态）
        self.queens[row] = col


    def remove_queen(self, row: int) -> None:
        #移除指定位置的皇后（还原棋盘状态）
        self.queens[row] = -1

    def solve(self) -> list:
        #求解八皇后问题，返回所有合法解
        solutions = []
        def backtrack(row):

            if row == self.size:
                solutions.append(self.queens[:])
                return

            for col in range(self.size):
                if self.is_safe(row, col):
                    self.place_queen(row, col)
                    backtrack(row + 1)
                    self.remove_queen(row)

        backtrack(0)
        return solutions


# ========== 测试示例 ==========
if __name__ == "__main__":
    # 创建八皇后实例
    queens = EightQueens(8)

    # 调用求解方法（返回所有解）
    solutions1 = queens.solve()

    # 打印解的个数
    print(f"共找到 {len(solutions1)} 个解。")