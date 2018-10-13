# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.


def rotate(words, n):
    s = ''
    for letter in words:
        if letter == ' ':
            s += ' '
        if letter != ' ':
            if (ord(letter) + n) >= 122:
                s += chr(ord(letter) - 26 + n)
            elif (ord(letter) + n) <= 96:
                s += chr(ord(letter) + 26 + n)
            # 如果用if空格会执行两次
            else:
                s += chr(ord(letter) + n)
    return s
# Your code here


print(rotate('sarah', 13))
# >>> 'fnenu'
print(rotate('fnenu', -13))
# >>> 'sarah'
print(rotate('dave', 5))
# >>>'ifaj'
print(rotate('ifaj', -5))
# >>>'dave'
print(rotate("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj", -17))
# >>> ???
