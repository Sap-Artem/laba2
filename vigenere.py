def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    mas = []
    for i in range(0, len(plaintext)):
        mas.append(ord(plaintext[i]))
    i = 0
    while(len(keyword)<len(plaintext)):
        keyword = keyword + keyword[i]
        i = i + 1
        if(i>=len(keyword)):
            i = 0
    mas_key = []
    for i in range(0, len(keyword)):
        shrift_key = ord(keyword[i])
        if(shrift_key > 96) & (shrift_key < 123):
            shrift_key = shrift_key - 97
        if(shrift_key > 64) & (shrift_key < 91):
            shrift_key = shrift_key - 65
        mas_key.append(shrift_key)
    for i in range(0,len(plaintext)):
        shifr_i = mas[i]
        if (mas[i] > 64) & (mas[i] < 91):
            shifr_i = shifr_i + mas_key[i]
            if shifr_i>90:
                shifr_i = shifr_i - 26
            else:
                if shifr_i<65:
                    shifr_i = shifr_i + 26
        else:
            if (mas[i] > 96) & (mas[i] < 123):
                shifr_i = shifr_i + mas_key[i]
                if shifr_i > 122:
                    shifr_i = shifr_i - 26
                else:
                    if shifr_i < 97:
                        shifr_i = shifr_i + 26
        ciphertext = ciphertext + chr(shifr_i)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    mas = []
    for ch in range(0, len(ciphertext)):
        mas.append(ord(ciphertext[ch]))
    ch = 0
    while (len(keyword) < len(ciphertext)):
        keyword = keyword + keyword[ch]
        ch = ch + 1
        if (ch >= len(keyword)):
            ch = 0
    mas_key = []
    for ch in range(0, len(keyword)):
        shrift_key = ord(keyword[ch])
        if (shrift_key > 96) & (shrift_key < 123):
            shrift_key = shrift_key - 97
        if (shrift_key > 64) & (shrift_key < 91):
            shrift_key = shrift_key - 65
        mas_key.append(shrift_key)
    for ch in range(0, len(ciphertext)):
        shifr_i = mas[ch]
        if (mas[ch] > 64) & (mas[ch] < 91):
            shifr_i = shifr_i - mas_key[ch]
            if shifr_i > 90:
                shifr_i = shifr_i - 26
            else:
                if shifr_i < 65:
                    shifr_i = shifr_i + 26
        else:
            if (mas[ch] > 96) & (mas[ch] < 123):
                shifr_i = shifr_i - mas_key[ch]
                if shifr_i > 122:
                    shifr_i = shifr_i - 26
                else:
                    if shifr_i < 97:
                        shifr_i = shifr_i + 26
        plaintext = plaintext + chr(shifr_i)
    return plaintext