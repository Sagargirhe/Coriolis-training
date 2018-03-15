#Write a version of a palindrome recogniser that accepts a file name from the user, reads each line, and prints the line to the screen if it is a palindrome.

from Q8 import isPalindrome

def print_palindromes(file_name):
    f = open(file_name,'r+')
    for line in f:
        if isPalindrome(line[:-1]):
            print (line)
    f.close()

print_palindromes('32.txt')
