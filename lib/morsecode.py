morsedict = {'A':'.-', 'B':'-...',
            'C':'-.-.', 'D':'-..', 'E':'.',
            'F':'..-.', 'G':'--.', 'H':'....',
            'I':'..', 'J':'.---', 'K':'-.-',
            'L':'.-..', 'M':'--', 'N':'-.',
            'O':'---', 'P':'.--.', 'Q':'--.-',
            'R':'.-.', 'S':'...', 'T':'-',
            'U':'..-', 'V':'...-', 'W':'.--',
            'X':'-..-', 'Y':'-.--', 'Z':'--..',
            '1':'.----', '2':'..---', '3':'...--',
            '4':'....-', '5':'.....', '6':'-....',
            '7':'--...', '8':'---..', '9':'----.',
            '0':'-----', ', ':'--..--', '.':'.-.-.-',
            '?':'..--..', '/':'-..-.', '-':'-....-',
            '(':'-.--.', ')':'-.--.-','Ą':'. - . - ', 
            'Ć':'- . - ..','Ę':'.. - .. ', 'Ó':'- - - . ',
            'Ś':'... - ...', 'Ź':'- - .. - .','Ń':'--.--',
            'Ż':'- - .. -','Ł':'. - .. - '}
def morseEncrypt(message):
    encryptedText = ''
    for letter in message.upper():
        if letter != ' ':
            encryptedText = encryptedText + morsedict.get(letter) + ' '
        else:
            encryptedText = encryptedText + ' '
    return encryptedText

def morseDecrypt(message):  #tą część podjebałem bo nie chcialo mi sie pisac
    message += ' '
    decipher = ''
    mycitext = ''
    for myletter in message:
        if (myletter != ' '):
            i = 0
            mycitext += myletter
        else:
            i += 1
            if i == 2 :
                decipher += ' '
            else:
                decipher += list(morsedict.keys())[list(morsedict.values()).index(mycitext)]
                mycitext = ''
    return decipher

