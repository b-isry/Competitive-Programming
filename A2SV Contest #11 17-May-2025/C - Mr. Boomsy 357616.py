# Problem: C - Mr. Boomsy - https://codeforces.com/gym/605795/problem/C

t = int(input())
for _ in range(t):
    s = input()
    st = []
    for c in s:
        if c == 'B' and st and st[-1] in 'AB':
            st.pop()
        else:
            st.append(c)
    print(len(st))