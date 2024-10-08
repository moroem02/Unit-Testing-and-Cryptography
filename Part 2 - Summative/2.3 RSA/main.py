import math
from sympy import nextprime
from random import randint
# Copy and paste any functions you need from the Affine assignment!

# Also write these:
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def mod_inverse_helper(a, b):
  q, r = a // b, a % b
  if r == 1:
    return (1, -1 * q)
  u, v = mod_inverse_helper(b, r)
  return (v, -1 * q * v + u)


def mod_inverse(a, m):
  assert math.gcd(a, m) == 1, "You're trying to invert " + str(a) + " in mod " + str(m) + " and that doesn't work!"
  return mod_inverse_helper(m, a)[1] % m


def rsa_encode(text, m, e):
  num = 0
  for i in range(len(text)):
    if text[i].upper() in alpha:
      x = alpha.find(text[i].upper())
      y = 26 ** i
      num += x * y
  if num < m:
    return pow(num,e,m)
  else:
    return "String too long!"


def rsa_decode(num, m, d, l):
  new_text = ""
  x = pow(num, d, m)
  for i in range(l):
    new_text += alpha[x % 26]
    x = x // 26
  return new_text

def get_d(p, q, e):
  t =  (p-1) * (q-1)
  return mod_inverse(e, t)



text = "THEFIVEBOXINGWIZARDSJUMPQUICKLY"
l = len(text)
p = 292361466231755597564095925310764764819
q = 307125506157764866722739041634199200019
e = 65537
m = p * q
d = get_d(p, q, e)
enc = rsa_encode(text, m, e)
dec = rsa_decode(enc, m, d, l)
print(enc)
print(dec)
#If this works, dec should be the same as text!


# Part 2: Generate your own key!
def make_prime(n):
  lower = 2 ** (n - 1) + 1
  upper = 2 ** n - 1
  temp = randint(lower, upper)
  return nextprime(temp)


p = make_prime(100)
q = make_prime(100)
e = 65537
m = p * q
d = get_d(p, q, e)
message = "FUNNEWMESSAGE"
l = len(message)
encoded = rsa_encode(message, m, e)
print(encoded)
print(rsa_decode(encoded, m, d, l))
