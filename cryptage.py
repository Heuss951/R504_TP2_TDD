import string

caracteres = string.ascii_lowercase

def crypt(message):
    result = ""
    for c in message:
        index = caracteres.index(c)
        result += caracteres[(index + 1) % len(caracteres)]
    return result
