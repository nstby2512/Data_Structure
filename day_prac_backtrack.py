#M04123：马走日

#当下的位置就是first
def possible_position(x, y):
    return [[x+1, y+2], [x-1, y+2], [x+1, y-2], [x-1, y-2],[x+2, y+1],[x-2,y+1], [x+2, y-1],[x-2, y-1]]

# ans = 0 global前要用
def horse(n, m, position_now, matrix, cnt):
    global ans
    #每到一个位置先变为true，离开时候别忘了false

    if 0<=position_now[0]<=(n-1) and 0<= position_now[1]<=(m-1) and matrix[position_now[0]][position_now[1]] == False:
        matrix[position_now[0]][position_now[1]] = True
    else:
        return

    #列出下一个位置的可能性
    next_position = possible_position(position_now[0], position_now[1])

    #计算当前是否是一个遍历完成的状态（是否走满了）
    if cnt == n * m:
        ans += 1
    #dfs
    for tmp in range(8):
        horse(n, m, next_position[tmp], matrix, cnt + 1)
    
    matrix[position_now[0]][position_now[1]] = False
    return
def input_func():
    t = int(input())
    for _ in range(t):
        ans = 0
        cnt = 1
        n, m, x, y = map(int, input().split())
        matrix = [([False]* m) for i in range(n)]
        horse(n, m, [x, y], matrix, cnt)
        print(ans)

    
def sub_set(nums, first = 0):
    for i in range(first, n):
        nums[first], nums[i] = nums[i], nums[first]
        res.append(nums[:first + 1])
        sub_set(nums, first + 1)
        nums[first], nums[i] = nums[i], nums[first]
    
