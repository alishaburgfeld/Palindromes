def palindrome(word):
    alphanumeric=""
    alphabet="abcdefghijklmnopqrstuvwxyz"
    numbers="1234567890"
    for char in str(word):
        if char in numbers:
            alphanumeric+=char
        if char.lower() in alphabet:
            alphanumeric+=char.lower()
    #print(str(alphanumeric))
    #print((str(alphanumeric))[::-1])
    return str(alphanumeric)== (str(alphanumeric))[::-1]

#print(palindrome('A man, a plan, a canal -- Panama'))
