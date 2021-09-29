# -*- coding: utf-8 -*-

# ABC131B問題
def test131B(n,l):
    n = list(range(l, l+n))

    if min(n) >= 0:
        n.remove(min(n))
    elif min(n) < 0 < max(n):
         n.remove(0)
    else:
        n.remove(max(n))
    print(sum(n))

test131B(30,-50)

def test132B(n,p):
    result = 0
    for i in range(0,n - 2):
        q = [p[i],p[i + 1],p[i + 2]]
        sorted_q = sorted(q)
        if sorted_q[1] == q[1]:
            result += 1
        
    
    print(result)


test132B(9,[9,6,3,2,5,8,7,4,1])

