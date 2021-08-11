from timeit import default_timer as timer


class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ["[.]" if i == "." else i for i in address]
        return "".join(ans)


start = timer()
solution = Solution()
print(solution.defangIPaddr("250.100.100.1"))
end = timer()
print((end - start) * 1000)
