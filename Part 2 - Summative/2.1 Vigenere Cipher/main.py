# Read the instructions to see what you need to do here!

#spaces included
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

def vig_encode(text, keyword):
  new_text = ""
  kindex = 0
  for i in range(len(text)):
    if text[i].upper() in alpha:
      if kindex > len(keyword)-1:
        kindex = 0
      new_character = alpha.find(keyword[kindex])+alpha.find(text[i].upper())
      if new_character > 26:
        new_character -= 27
      new_text += alpha[new_character]
      kindex += 1
    else:
      new_text += text[i]
  return new_text


def vig_decode(text, keyword):
  new_text = ""
  kindex = 0
  for i in range(len(text)):
    if text[i].upper() in alpha:
      if kindex > len(keyword)-1:
        kindex = 0
      character = alpha.find(text[i].upper())-alpha.find(keyword[kindex])
      if character < 0:
        character += 27
      new_text += alpha[character]
      kindex += 1
    else:
      new_text += text[i]
  return new_text


test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
vig_key = "TEST"
enc = vig_encode(test, vig_key)
dec = vig_decode(enc, vig_key)
print(enc)
print(dec)
# If this worked, dec should be the same as test!