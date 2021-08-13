# class Solution:
#     def judgeCircle(self, moves: str) -> bool:
#         x, y = 0, 0
#         for move in moves:
#             if move == "U":
#                 y += 1
#             elif move == "D":
#                 y -= 1
#             elif move == "R":
#                 x += 1
#             elif move == "L":
#                 x -= 1
#         return x == 0 and y == 0


# class Solution:
#     def judgeCircle(self, moves: str) -> bool:
#         counter = {}
#         for move in moves:
#             counter[move] = counter.get(move, 0) + 1
#         return counter.get("U") == counter.get("D") and counter.get("L") == counter.get(
#             "R"
#         )


# class Solution:
#     def judgeCircle(self, moves: str) -> bool:
#         x = moves.count("L") - moves.count("R")
#         y = moves.count("U") - moves.count("D")
#         return x == 0 and y == 0


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = moves.count("L") == moves.count("R")
        y = moves.count("U") == moves.count("D")
        return x and y


solution = Solution()
print(solution.judgeCircle("UD"))
