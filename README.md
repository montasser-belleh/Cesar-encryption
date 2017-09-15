# Cesar-encryption
Cesar encryption is one of the oldest cryptography methods knowen to humans , yet using a random module to encrypt files makes it harder to decrypt , in this code I am using Zipf's law on English/French language to Decrypt 

Modules required : Random

Zipf's Law

In the English language, the probability of encountering the rth most common word is given roughly by P(r)=0.1/r for r up to 1000 or so. The law breaks down for less frequent words, since the harmonic series diverges. Pierce's (1980, p. 87) statement that sumP(r)>1 for r=8727 is incorrect. Goetz states the law as follows: The frequency of a word is inversely proportional to its statistical rank r such that
P(r) approx 1/(rln(1.78R)),

where R is the number of different words. 


The idea here , for example , is that the word "The" is the most occuring in english , among other words , this makes the letter "E" the most frequent , the trick is to find the most occuring letter in the encrypted file , try to make it "E" , thus finding the step of encryption , of course in this code , the encryption step is random , using the Random module .
 
Example : 
"abcedfghijklmnopqrstuvwxyz" where "A" is 1 , "Z" is 26
if the encrypting step is 3 , the letter "A" becomes a "D" , "B" becomes an "E" , "Y" becomes a "B" , and "Z" becomes a "C"
if the encrypting step is p (random integer) , and the most occuring letter in a text is "H" , than to make "E" and "H" p must be 3



Inspired by https://youtu.be/fCn8zs912OE
More about Zipf's law http://mathworld.wolfram.com/ZipfsLaw.html
