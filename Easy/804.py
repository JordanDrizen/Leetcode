from typing import List


# class Solution:

#     morse = {
#         "A": ".-",
#         "B": "-...",
#         "C": "-.-.",
#         "D": "-..",
#         "E": ".",
#         "F": "..-.",
#         "G": "--.",
#         "H": "....",
#         "I": "..",
#         "J": ".---",
#         "K": "-.-",
#         "L": ".-..",
#         "M": "--",
#         "N": "-.",
#         "O": "---",
#         "P": ".--.",
#         "Q": "--.-",
#         "R": ".-.",
#         "S": "...",
#         "T": "-",
#         "U": "..-",
#         "V": "...-",
#         "W": ".--",
#         "X": "-..-",
#         "Y": "-.--",
#         "Z": "--..",
#     }

#     def uniqueMorseRepresentations(self, words: List[str]) -> int:
#         ans = []
#         for word in words:
#             ans.append("".join((list(map(lambda x: self.morse[x.upper()], word)))))
#         return len(set(ans))


class Solution:

    morse = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        ans = set()
        for word in words:
            ans.add("".join((list(map(lambda x: self.morse[x.upper()], word)))))
        return len(ans)


solution = Solution()
print(solution.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
