n = int(input())
ans = {}

for i in range(n):
    m = input()
    name, size = m.split("-")
    if name in ans:
        ans[name].append(size)
    else:
        ans[name] = [size]

for k in sorted(ans.keys()):
    v = ans[k]
    m_list = []
    b_list = []
    for i in v:
        if i.endswith("B"):
            b_list.append(i)
        else:
            m_list.append(i)
    
    m_list.sort(key=lambda x: float(x[:-1]))
    b_list.sort(key=lambda x: float(x[:-1]))
    
    v_sorted = m_list + b_list
    print(f"{k}: {', '.join(v_sorted)}")
