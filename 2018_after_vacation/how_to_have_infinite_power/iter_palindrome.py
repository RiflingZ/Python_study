def iter_palindrome(s):
    for i in range(0, int(len(s) / 2)):
        if s[i] != s[-(i + 1)]:
            return False
    return True
    ## 迭代,在Python中尽量采用非递归方式


print(iter_palindrome(''))
# >>> True
print(iter_palindrome('abab'))
# >>> False
print(iter_palindrome('abba'))
# >>> True

