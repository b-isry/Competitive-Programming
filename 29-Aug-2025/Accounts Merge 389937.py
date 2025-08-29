# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        root = {}
        acc = {}  

        def find(x):
            if x != root[x]:
                root[x] = find(root[x])  
            return root[x]

        def union(x, y):
            p1, p2 = find(x), find(y)
            if p1 != p2:
                root[p2] = p1

        for account in accounts:
            name = account[0]
            first = account[1]

            for email in account[1:]:
                if email not in root:
                    root[email] = email
                union(first, email)
                acc[email] = name

        emails = defaultdict(list)
        for email in root:
            par = find(email)
            emails[par].append(email)
        
        ans = []
        for par, email in emails.items():
            name = acc[par]
            ans.append([name] + sorted(email))

        return ans

