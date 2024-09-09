# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def sub_encode(text, codebet):
    new_text = ""
    for i in range(len(alpha)):
        if alpha[i] not in codebet:
            codebet += alpha[i]
    for i in range(len(text)):
        if text[i].upper() in alpha:
            x = alpha.find(text[i].upper())
            new_text += codebet[x]
        else:
            new_text += text[i]
    return new_text


def sub_decode(text, codebet):
    new_text = ""
    for i in range(len(alpha)):
        if alpha[i] not in codebet:
            codebet += alpha[i]
    for i in range(len(text)):
        if text[i].upper() in alpha:
            x = codebet.find(text[i].upper())
            new_text += alpha[x]
        else:
            new_text += text[i]
    return new_text


test = "HELLOWORLD"
cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
enc = sub_encode(test, cipher_alphabet)
dec = sub_decode(enc, cipher_alphabet)
print(enc)
print(dec)
# If this worked, dec should be the same as test!

