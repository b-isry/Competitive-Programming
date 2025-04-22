# Problem: First Unique Character in a String - https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=queue

class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_cnt = Counter(s)

        for i,ltr in enumerate(s):
            if s_cnt[ltr] == 1:
                return i
        return -1



        