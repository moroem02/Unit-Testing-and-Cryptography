# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def sub_encode(text, codebet):
    new_text = ""
    for i in range(len(text)):
        x = alpha.find(text[i])
        new_text += codebet[x]
    return new_text


def sub_decode(text, codebet):
    new_text = ""
    for i in range(len(text)):
        x = codebet.find(text[i])
        new_text += alpha[x]
    return new_text


test = "HELLOWORLD"
cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
enc = sub_encode(test, cipher_alphabet)
dec = sub_decode(enc, cipher_alphabet)
print(enc)
print(dec)
# If this worked, dec should be the same as test!

