# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar_encode(text, n):
    new_text = ""
    for i in range(len(text)):
        if text[i] in alpha:
            x = alpha.find(text[i].upper())
            if x+n > 25:
                new_text += alpha[(x + n)-25]
            else:
                new_text += alpha[x+n]
        else:
            new_text += text[i]
    return new_text


def caesar_decode(text, n):
    new_text = ""
    for i in range(len(text)):
        x = alpha.find(text[i].upper())
        if x - n <0:
            new_text += alpha[(x - n) + 25]
        else:
            new_text += alpha[x - n]
    return new_text


test = "HELLO WORLD"
shift = 5
enc = caesar_encode(test, shift)
dec = caesar_decode(enc, shift)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
