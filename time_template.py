from timeit import default_timer as timer

start = timer()
solution = Solution()
print(solution.defangIPaddr("250.100.100.1"))
end = timer()
print((end - start) * 1000)
