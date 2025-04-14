# Problem: Largest Merge of Two Strings - https://leetcode.com/problems/largest-merge-of-two-strings/

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i = j = 0
        merge = []
        n = len(word1)
        m = len(word2)

        while i < n and j < m:
            if word1[i:] > word2[j:]:
                merge.append(word1[i])
                i += 1
            else:
                merge.append(word2[j])
                j += 1

        merge.extend(word1[i:])
        merge.extend(word2[j:])

        return "".join(merge)


