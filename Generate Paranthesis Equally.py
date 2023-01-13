def Parenthesis(str, n):
    if(n > 0):
        generateParenthesis(str, 0, n, 0, 0)

 
def generateParenthesis(str, pos, n , open,close):
    if close == n:
        for i in str:
            print(i, end="")
        print()
    
    else:
        if open > close:
            str[pos] = ")"
            generateParenthesis(str,pos+1, n, open, close+1)
        if open < n:
            str[pos] = "("
            generateParenthesis(str,pos+1, n, open+1, close)
n = int(input())
str = [""] * 2 * n
Parenthesis(str, n)