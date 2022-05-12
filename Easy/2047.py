import re


class Solution:
    def countValidWords(self, sentence: str) -> int:
        ans = 0
        if sentence == sentence.lower() and len(re.findall(r'[0-9]', sentence)) == 0:
            sentence = sentence.split()
            print(sentence)
            for word in sentence:
                if '-' in word and word.count('-') > 1:
                    continue
                elif '-' in word and word.count('-') == 1 and (word.index('-') == 0 or word.index('-') == len(word) - 1):
                    continue
                elif '-' in word and word.count('-') == 1 and not word[word.index('-') - 1].isalpha() and not word[word.index('-') + 1].isalpha():
                    continue
                else:
                    print(word)
        return ans


solution = Solution()
print(solution.countValidWords("ca-t and  dog"))
