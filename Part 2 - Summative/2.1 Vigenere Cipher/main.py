# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def vig_encode(text, keyword):
  new_text = ""
  kindex = 0
  for i in range(len(text)):
    if kindex > len(keyword)-1:
      kindex = 0
    new_character = alpha.find(keyword[kindex])+alpha.find(text[i])
    if new_character > 25:
      new_character -= 26
    new_text += alpha[new_character]
    kindex += 1
  return new_text


def vig_decode(text, keyword):
  return ""


test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
vig_key = "TEST"
enc = vig_encode(test, vig_key)
dec = vig_decode(enc, vig_key)
print(enc)
print(dec)
# If this worked, dec should be the same as test!