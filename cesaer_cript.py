def caesar_eng_cryp():
    k = int(input('key '))
    s, word = input('word '), ''
    for c in s:
        if 0 <= ord(c) <= 64 or 91 <= ord(c) <= 96 or 123 <= ord(c) <= 1039 or ord(c) > 1103:
            word += c
        else:
            if ord(c) + k <= 122 and c.islower():
                word += chr(ord(c) + k)
            elif ord(c) + k > 122 and c.islower():
                word += chr((ord(c) + k) % 122 + 96)
            elif ord(c) + k <= 90 and c.isupper():
                word += chr(ord(c) + k)
            elif ord(c) + k > 90 and c.isupper():
                word += chr((ord(c) + k) % 90 + 64)
    print(word)

def caesar_rus_cryp():
    k = int(input('key '))
    s, word = input('word '), ''
    for c in s:
        if 0 <= ord(c) <= 64 or 91 <= ord(c) <= 96 or 124 <= ord(c) <= 1039 or ord(c) > 1103:
            word += c
        else:
            if ord(c) + k <= 1103 and c.islower():
                word += chr(ord(c) + k)   
            elif ord(c) + k > 1103 and c.islower():
                word += chr((ord(c) + k) % 1103 + 1071)
            elif ord(c) + k <= 1071 and c.isupper():
                word += chr(ord(c) + k)
            elif ord(c) + k > 1071 and c.isupper():
                word += chr((ord(c) + k) % 1071 + 1039)
    print(word)
    
def caesar_eng_decryp():
    k = int(input('key '))
    s, word = input('word '), ''
    for c in s:
        if 0 <= ord(c) <= 64 or 91 <= ord(c) <= 96 or 124 <= ord(c) <= 1039 or ord(c) > 1103:
            word += c
        else:
            if ord(c) - k < 97 and c.islower():
                word += chr((ord(c) - k) % 97 + 26)
            elif ord(c) - k >= 97 and c.islower():
                word += chr(ord(c) - k)
            elif ord(c) - k < 65 and c.isupper():
                word += chr((ord(c) - k) % 65 + 26)
            elif ord(c) - k >= 97 and c.isupper():
                word += chr(ord(c) - k)
    print(word)            
            
def caesar_rus_decryp():
    k = int(input('key '))
    s, word = input('word '), ''    
    for c in s:
        if 0 <= ord(c) <= 64 or 91 <= ord(c) <= 96 or 124 <= ord(c) <= 1039 or ord(c) > 1103:
            word += c
        else:
            if ord(c) - k < 1072 and c.islower():
                word += chr((ord(c) - k) % 1072 + 32)
            elif ord(c) - k >= 1072 and c.islower():
                word += chr(ord(c) - k)
            elif ord(c) - k < 1040 and c.isupper():
                word += chr((ord(c) - k) % 1047 + 32)
            elif ord(c) - k >= 1040 and c.isupper():
                word += chr(ord(c) - k)            
    print(word)            
            
cryp_or_decryp = input('Выберите шифровку/дешифровку (cryp/decryp) ')
cryp_or_decryp = cryp_or_decryp.lower()
language = input('Выберите язык для шифрования/дешифрования (rus/eng) ')
language = language.lower()

if cryp_or_decryp == 'cryp':
    if language == 'eng':
        caesar_eng_cryp()
    elif language == 'rus':
        caesar_rus_cryp()
        
elif cryp_or_decryp == 'decryp':
    if language == 'eng':
        caesar_eng_decryp()
    elif language == 'rus':
        caesar_rus_decryp()    