
def findKthLargest( nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    if not nums:
        return None
    def quicksort(nums,s,t):
        i = s
        j = t
        if s<t:
            tmp = nums[s]
        if s<t:
            while i!=j:
                while i<j and nums[j]>tmp:
                    j-=1
                if i<j:
                    nums[i] = nums[j]
                    i+=1
                while i<j and nums[i]<tmp:
                    i+=1
                if i<j:
                    nums[j] = nums[i]
                    j-=1
            nums[i] = tmp
        # if i>len(nums)-k:
            quicksort(nums, s,i-1)
        # elif i==len(nums)-k:
        #     return tmp
        # else:
            quicksort(nums, i+1,t)
    quicksort(nums,0,len(nums)-1)
    return nums[len(nums)-k]

if __name__ =="__main__":
    nums = [2,1]
    k = 1
    print(findKthLargest(nums, k))
