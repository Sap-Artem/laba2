def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    mas = []
    for i in range(0,len(plaintext)):
        mas.append(ord(plaintext[i]))
    for i in range(0,len(plaintext)):
        shifr_i = mas[i]
        if (mas[i] > 64) & (mas[i] < 91):
            shifr_i = shifr_i + shift
            if shifr_i>90:
                shifr_i = shifr_i - 26
            else:
                if shifr_i<65:
                    shifr_i = shifr_i + 26
        else:
            if (mas[i] > 96) & (mas[i] < 123):
                shifr_i = shifr_i + shift
                if shifr_i > 122:
                    shifr_i = shifr_i - 26
                else:
                    if shifr_i < 97:
                        shifr_i = shifr_i + 26
        ciphertext = ciphertext + chr(shifr_i)
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    mas = []
    for ch in range(0, len(ciphertext)):
        mas.append(ord(ciphertext[ch]))
    for ch in range(0, len(ciphertext)):
        shifr_i = mas[ch]
        if (mas[ch] > 64) & (mas[ch] < 91):
            shifr_i = shifr_i - shift
            if shifr_i > 90:
                shifr_i = shifr_i - 26
            else:
                if shifr_i < 65:
                    shifr_i = shifr_i + 26
        else:
            if (mas[ch] > 96) & (mas[ch] < 123):
                shifr_i = shifr_i - shift
                if shifr_i > 122:
                    shifr_i = shifr_i - 26
                else:
                    if shifr_i < 97:
                        shifr_i = shifr_i + 26
        plaintext = plaintext + chr(shifr_i)
    return plaintext