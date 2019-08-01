
def lengthOfLIS( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    size = len(nums)
    if size <= 1:
        return size

    tails = [nums[0]]
    ans = 0

    for x in nums[1:]:
        if x > tails[-1]:
            tails.append(x)
        else:  # replace this to the most potential position
            beg, end = 0, len(tails)
            while beg != end:
                mid = (beg + end) // 2
                if tails[mid] < x:
                    beg = mid + 1
                else:
                    end = mid
            tails[beg] = x

    return len(tails)
if __name__ =="__main__":
    d = [10,9,2,5,3,7,101,18]
    print(lengthOfLIS(d))
