# -*- coding: utf-8 -*-

# ABC131B問題
def test(n,l):
    n = list(range(l, l+n))

    if min(n) >= 0:
        n.remove(min(n))
    elif min(n) < 0 < max(n):
         n.remove(0)
    else:
        n.remove(max(n))
    print(sum(n))

test(30,-50)