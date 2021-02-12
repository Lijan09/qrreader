characters = {
    'a': '013',
    'b': '014',
    'c': '015',
    'd': '016',
    'e': '017',
    'f': '018',
    'g': '019',
    'h': '020',
    'i': '021',
    'j': '022',
    'k': '023',
    'l': '024',
    'm': '025',
    'n': '026',
    'o': '027',
    'p': '028',
    'q': '029',
    'r': '030',
    's': '031',
    't': '032',
    'u': '033',
    'v': '034',
    'w': '035',
    'x': '036',
    'y': '037',
    'z': '038',
    '0': '099',
    '1': '098',
    '2': '097',
    '3': '096',
    '4': '095',
    '5': '094',
    '6': '093',
    '7': '092',
    '8': '091',
    '9': '090',
    ' ': '089'
}


def encrypt(message):
    global characters
    encrypted = ''
    for char in message:
        value = characters.get(char)
        encrypted += value
    return encrypted


def decrypt(message):
    global characters
    decrypted = []
    numbers = []
    individualNum = 0
    lastNumber = 0
    letter = []
    count = 0
    for i in range(len(message)):
        if (i+1) % 3 == 0:
            individualNum = message[lastNumber: i + 1]
            numbers.append(individualNum)
            lastNumber = i+1

    values = list(characters.values())
    keys = list(characters.keys())
    for i in range(len(numbers)):
        index = values.index(numbers[i])
        letter = keys[index]
        decrypted += letter
    return ''.join(decrypted)
