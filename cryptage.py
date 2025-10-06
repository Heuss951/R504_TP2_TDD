import string

caracteres = string.ascii_lowercase

def crypt(message, pas=1):
    result = ""
    for c in message:
        index = caracteres.index(c)
        result += caracteres[(index + pas) % len(caracteres)]
    return result + str(pas)
