class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        if letters.index(coordinates[0]) % 2 == 0 and int(coordinates[1]) % 2 != 0:
            return False
        elif letters.index(coordinates[0]) % 2 != 0 and int(coordinates[1]) % 2 == 0:
            return False
        return True


solution = Solution()
print(solution.squareIsWhite("h8"))
