# Problem: B - Aaron and Repeated Letters - https://codeforces.com/gym/605795/problem/B

python s=input() st=[] for c in s: if st and st[-1]==c: st.pop() else: st.append(c) print(''.join(st))