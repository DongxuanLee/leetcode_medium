
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    if not s:
        return None
    start = 0
    end = 0
    for i in range(len(s)):
        len1 = expandAroundCenter(s,i,i)
        len2 = expandAroundCenter(s, i, i+1)
        llen = max(len1,len2)
        if llen-1>(end-start):
            start = i-(llen-1)//2
            end = i + llen//2
    return s[start:end+1]
def expandAroundCenter(s,left,right):
    while left>=0 and right<len(s) and s[left]==s[right]:
        left -=1
        right +=1
    return right-left-1

if __name__ == '__main__':
    k = "babad"

    print(longestPalindrome(k))
