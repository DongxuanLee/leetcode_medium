
def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    # parentheses = ['(',')']
    output = []
    def backtrack(out,leftn,rightn,resn):
        if leftn == rightn and leftn== n:
            output.append(out)
        else:
            if resn>0:
                backtrack(out+'(',leftn+1,rightn,resn-1)
            if rightn<leftn:
                backtrack(out+')',leftn,rightn+1,resn)
    if n>0:
        backtrack('',0,0,n)
    return output

if __name__ =="__main__":
    d = 0
    print(generateParenthesis(d))