import numpy as np

def factors(x):
    ct = 0
    for i in range(2, np.int32((x/2)+1)):
        if(x%i == 0):
            ct = ct + 1; 
    return ct

    
def encrypt(num, public_key):
    val = (num**public_key[0]) % public_key[1]
    return val

def decrypt(num, public_key):
    fac = np.array([0, 0])
    fac1 = 0
    fac2 = 0
    a = 0
    j = 0
    
    for i in range(2, np.int32(public_key[1]/2)+1):
        if(public_key[1]%i == 0):
            if(factors(i) == 0):
                if(j == 0):
                    fac = fac + np.array([i,0])
                else: 
                    fac = fac + np.array([0,i])
            j = j + 1

            
    fac1 = fac[0]
    fac2 = fac[1]
    
    for a in range(0, 10000):
        if((public_key[0]*a) % ((fac1 - 1) * (fac2 - 1)) == 1):
            break
            
    val = (num**a) % public_key[1]
    return val
    
    def encryptMessage(sequence):
    encryptedSequence = ""
    encryptedChar = ''
    ct = 0
    
    for i in range(0, len(sequence)):
        char = sequence[i]
        
        if char == ' ':
            ct = ct + 1
            
        encryptedChar = chr(encrypt(ord(char), [5, 20711]) + 1750 + (i//5))
        encryptedSequence = encryptedSequence + encryptedChar
        
    return encryptedSequence

def decryptMessage(sequence):
    decryptedSequence = ""
    decryptedChar = ''
    ct = 0
    
    for i in range(0, len(sequence)):
        char = sequence[i]
        
        if char == ' ':
            ct = ct + 1
            
        decryptedChar = chr(decrypt(ord(char) - 1750 - (i//5), [5, 20711]))
        decryptedSequence = decryptedSequence + decryptedChar
        
    return decryptedSequence

def encryptMessageStrong(sequence):
    message = sequence
    for i in range(10):
        message = encryptMessage(message)
    return message

def decryptMessageStrong(sequence):
    message = sequence
    for i in range(10):
        message = decryptMessage(message)
    return message
