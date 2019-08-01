
def countSubstrings( s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0
    count =0
    for i in range(len(s)):
        count =expandAroundCenter(s,i,i,count)
        count =expandAroundCenter(s, i, i+1,count)
    return count
def expandAroundCenter(s,left,right,count):
    while left>=0 and right<len(s) and s[left]==s[right]:
        count +=1
        left -=1
        right +=1
    return count

if __name__ =="__main__":
    d = "aaa"
    print(countSubstrings(d))