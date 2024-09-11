import math

# Read the instructions to see what to do!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# PART 1
# These functions are provided for you!
def mod_inverse_helper(a, b):
    q, r = a//b, a%b
    if r == 1:
        return (1, -1 * q)
    u, v = mod_inverse_helper(b, r)
    return (v, -1 * q * v + u)

def mod_inverse(a, m):
    assert math.gcd(a, m) == 1, "You're trying to invert " + str(a) + " in mod " + str(m) + " and that doesn't work!"
    return mod_inverse_helper(m, a)[1] % m


# These are the functions you'll need to write:
def affine_encode(text, a, b):
    new_text = ""
    for i in range(len(text)):
        if text[i] in alpha:
            x = alpha.find(text[i].upper())
            lnum = (a * x + b) % 26
            new_text += alpha[lnum]
        else:
            new_text += text[i]
    return new_text

def affine_decode(text, a, b):
    new_text = ""
    for i in range(len(text)):
        if text[i] in alpha:
            x = alpha.find(text[i].upper())
            lnum = (x-b) * mod_inverse(a,26) % 26
            new_text += alpha[lnum]
        else:
            new_text += text[i]
    return new_text

test = "HELLOWORLD"
a = 3
b = 9
enc = affine_encode(test, a, b)
dec = affine_decode(enc, a, b)
print(enc)
print(dec)
# If this worked, dec should be the same as test!



# PART 2
# These  are the functions you'll need to write:
def convert_to_num(ngram):
    num = 0
    for i in range(len(ngram)):
        if ngram[i].upper() in alpha:
            x = alpha.find(ngram[i].upper())
            y =  26 ** i
            num += x * y
    return num

def convert_to_text(num, n):
    x = num
    new_text = ""
    for i in range(n):
        new_text += alpha[x % 26]
        x = x // 26
    return new_text

test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
l = len(test)
num = convert_to_num(test)
answer = convert_to_text(num, l)
print(num)
print(answer)
# If this worked, answer should be the same as test!



# PART 3

# These are the functions you'll need to write:
def affine_n_encode(text, n, a, b):
    return ''

def affine_n_decode(text, n, a, b):
    return ''

test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
n = 5
a = 347
b = 1721
enc = affine_n_encode(test, n, a, b)
dec = affine_n_decode(enc, n, a, b)
print(enc, dec)
# If this worked, dec should be the same as test!