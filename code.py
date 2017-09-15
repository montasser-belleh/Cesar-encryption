import random as rm
import cesar as cs
cond='y'
while cond=='y':
    msg=input('donnez votre message  :  ')
    test=input('voulez vous [crypter (c)/ decyrpter (d)] ? :  ' )
    if test=='c':
        print(cs.CryptCesarMessage(msg,rm.randint(1,26)))
    if test=='d':
        print(cs.dechiffrerMessage(msg))
    cond=input('voulez vous repeter ? [y/n]  ')
    
