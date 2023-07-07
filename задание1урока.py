def checkPalindrome(n):
    centr = len(n)//2
    for i in range(centr):
        if n[i]!=n[len(n)-1-i]:
            return False
    return True

print(checkPalindrome('лепсспел'))
