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

#test131B(30,-50)

# ABC132B問題
def test132B(n,p):
    result = 0
    for i in range(0,n - 2):
        q = [p[i],p[i + 1],p[i + 2]]
        sorted_q = sorted(q)
        if sorted_q[1] == q[1]:
            result += 1
        
    
    print(result)


#test132B(9,[9,6,3,2,5,8,7,4,1])

# 動的計画法を用いた部分和問題
def find_max_dp(num_list, limit):
    list_len = len(num_list)
    # ここで二次元配列を生成
    dp_table = [[0 for j in range(limit + 1)] for i in range(list_len)]
    
    for j in range(limit + 1):
        # 一列目について、最大値を超えなければ配列に入れる
        if num_list[0] <= j:
            dp_table[0][j] = list[0]
 
    for i in range(list_len):
        if i == 0:
            continue
        for j in range(limit + 1):
            if j == 0:
                continue
            # 最大値を超えた場合に、現在の二次元配列の場所に入れる値は、一つ前の値
            tmp_not_choice = dp_table[i-1][j]
            if num_list[i] > j:
                # もしnum_list[i](つまり、現在調査している数字)が最大値jを超える場合は、tmp_not_choiceを入れる
                dp_table[i][j] = tmp_not_choice 
            else:
                tmp_choice = dp_table[i-1][j - num_list[i]] + num_list[i]
                dp_table[i][j] = max(tmp_choice,tmp_not_choice)
    return dp_table[list_len - 1][limit]
 
list = [4,8,6]
print(find_max_dp(list,10))

def flog(n,h):
    dp = [0 for i in range(n)]
    
    for i in range(n):
        print(dp)
        if i == 0:
            dp[i] == 0
        elif i == 1:
            dp[i] = abs(h[i] - h[i - 1])
            print(dp[i])
        else:
             dp[i] = min(dp[i - 1] + abs(h[i] - h[i - 1]),dp[i - 2] + abs(h[i] - h[i - 2]))
             print("i",i)
             print(h)
             print(h[i - 1])
             print(abs(h[i] - h[i - 1]))
             print(h[i - 1] + abs(h[i] - h[i - 1]))
             print(h[i - 2])
             print(abs(h[i] - h[i - 2]))
             print(h[i - 2] + abs(h[i] - h[i - 2]))
    return dp[n - 1]
print(flog(7,[2,9,4,5,1,6,10]))

def abc081b(array,count = 0):
    odd_flag = True
    for i in array:
        if i % 2 != 0:
            odd_flag = False
    print(odd_flag)
    if odd_flag:
        for i in range(len(array)):
            array[i] = array[i] / 2
        count += 1
        abc081b(array,count)
    else:
        print(count)
        return array

abc081b([8,8,8])

def abc087b(x,a,b,c):
    result = 0
    for i in range(a + 1):
        for j in range(b + 1):
            for k in range(c + 1):
                print(i,j,k)
                sum = 500 * i + 100 * j + 50 * k
                print(sum)
                if x == sum:
                    result += 1

    print(result)

abc087b(100,2,2,2)

def abc083b(n,a,b):
    total = 0
    for i in range(1,n + 1):
        if a <= calceachNum(i) and calceachNum(i) <= b:
            total += i
    return total

def calceachNum(n):
    sum = 0
    while (n > 0):
        sum += n % 10
        n /= 10

    return sum

abc083b(20,2,5)

def abc088b(n,a):
    boy = 0
    girl = 0
    a.sort(reverse = True)
    for i in range(n):
        if i % 2 == 0:
            girl += a[i]
        else:
            boy += a[i]
    print(girl - boy)

abc088b(3,[2,7,4])

def abc085b(n,d):
    e = set(d)
    print(len(e))

abc085b(4,[6,6,8,9,2,2,9])
    

def abc085c(n,y):
    for i in range(n + 1):
        for j in range(n + 1):
            c = n - i - j
            sum = 10000 * i + 5000 * j + 1000 * c
            if sum == y:
                print(f"({i},{j},{c})")
                return
    
    print("(-1,-1,-1)")

abc085c(9,45000)