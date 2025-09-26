def binary_search(m_period, nums):
    r = sum(nums)
    l = max(nums)
    while l <= r:
        mid = (l + r) // 2
        tmp = 0
        cnt = 1
        for i in nums:
            tmp += i
            if tmp > mid :
                cnt += 1
                tmp = i
            if cnt > m_period:
                break
        if cnt > m_period:
            l = mid + 1
        else:
            r = mid - 1
    return l

n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]
print(binary_search(m, nums))



