#Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome("radar") should return True.

def isPalindrome(string):
    i = 0
    j = len(string) - 1
    while i <= j:
        if string[i]==string[j]:
            i+=1
            j=j-1
        else:
            return False
    return True

#print (isPalindrome("radarr"))

