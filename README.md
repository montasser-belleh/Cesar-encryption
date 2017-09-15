# Cesar-encryption
Cesar encryption is one of the oldest cryptography methods knowen to humans , yet using a random module to encrypt files makes it harder to decrypt , in this code I am using Zipf's law on English/French language to Decrypt .

''' Crypting '''
alphabet='abcdefghijklmnopqrstvuwxyz'

def Position(caractere):
    if caractere in alphabet :
        return alphabet.index(caractere)
    else :
        return 69

def CryptCesarCaractere(caractere,pas):
    if Position(caractere)!=69:
        return alphabet[(Position(caractere)+pas)%26]
    else:
        return caractere

def CryptCesarMessage(message,pas):
    crypted=''
    for i in range(len(message)):
        crypted+=CryptCesarCaractere(message[i],pas)
    return crypted

''' Decrypting '''


def LettreFrequence(message):
    liste=[]
    for i in range(len(alphabet)):
        if alphabet[i] in message:
            liste.append((alphabet[i],message.count(alphabet[i])))
    return liste

def MostOccuringLetter(liste):
    plusOccurante=0
    for i in range(1,len(liste)):
        if liste[i][1]>liste[plusOccurante][1]:
            plusOccurante=i
    return liste[plusOccurante][0]
 
def PasMessage(message): 
    x=MostOccuringLetter(LettreFrequence(message))
    pas=Position(x)-Position('e')
    return pas

def dechiffrerMessage(message):
    pas=PasMessage(message)
    return CryptCesarMessage(message,-pas)
