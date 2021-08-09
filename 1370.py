class Solution:
    def sortString(self, s: str) -> str:
        ans = ""
        counter = {}
        for letter in s:
            counter[ord(letter)] = counter.get(ord(letter), 0) + 1
        while counter:
            for num in sorted([*counter]):
                ans += chr(num)
                counter[num] -= 1
                if counter[num] == 0:
                    counter.pop(num)
            if counter:
                for num in sorted([*counter])[::-1]:
                    ans += chr(num)
                    counter[num] -= 1
                    if counter[num] == 0:
                        counter.pop(num)
        return ans


solution = Solution()
print(solution.sortString("aaaabbbbcccc"))
