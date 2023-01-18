def creat(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    result = [0, 1]
    for _ in range(n - 2):
        result.append(result[-1] + result[-2])
    return result


def locate(target, nums):
    for idx in range(len(nums)):
        current_num = nums[idx]
        if current_num == target:
            return idx
    return -1 

