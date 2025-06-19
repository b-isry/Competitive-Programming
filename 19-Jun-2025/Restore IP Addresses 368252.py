# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)
        if n > 12 and n < 4:
            return res
        
        def back(start, part):
            if len(part) == 4:
                if start == n:
                    res.append(".".join(part))
                return

            for i in (1, 2, 3):
                if start + i > n:
                    break
                seg = s[start : start + i]

                if seg[0] == '0' and i> 1:
                    continue

                val = int(seg)
                if val > 255:
                    continue
                part.append(seg)
                back(start + i, part)
                part.pop()

        back(0, [])
        return res