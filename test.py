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

# ABC132B問題
def test132B(n,p):
    result = 0
    for i in range(0,n - 2):
        q = [p[i],p[i + 1],p[i + 2]]
        sorted_q = sorted(q)
        if sorted_q[1] == q[1]:
            result += 1
        
    
    print(result)


test132B(9,[9,6,3,2,5,8,7,4,1])

# 動的計画法を用いた部分和問題
def find_max_dp(num_list, limit):
    list_len = len(num_list)
    dp_table = [[0 for j in range(limit + 1)] for i in range(list_len)]
 
    # 1番目のカード
    for j in range(limit + 1):
        if num_list[0] <= j:
            dp_table[0][j] = list[0] # 1番目のカードを追加
 
    # 2番目以降のカード
    for i in range(list_len):
        for j in range(limit + 1):
            tmp_not_choice = dp_table[i-1][j]
            if num_list[i] > j: # コスト不足のとき
                dp_table[i][j] = tmp_not_choice 
            else:
                tmp_choice = dp_table[i-1][j - num_list[i]] + num_list[i]
                dp_table[i][j] = max(tmp_choice,tmp_not_choice)
 
    return dp_table[list_len - 1][limit]
 
list = [4,8,6]
print(find_max_dp(list,10))

