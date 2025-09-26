def bs(nums, maxOperations):
    l = 1
    r = max(nums)
    ans = 0
    while l <= r :
        mid = (l + r) // 2
        ops = sum((x - 1) // mid for x in nums)
        if ops > maxOperations:
            l = mid + 1 #在[mid + 1, r]中
        else:
            r = mid - 1 #在[l, mid - 1]中找
    return l
        
nums = input()
nums = nums.split()
nums = [ int(n) for n in nums]
op = nums[-1]
nums = nums[: -1]
print(bs(nums, op))


