
import re,collections

wordstring = 'it was the best of times it was the worst of times '
wordstring += 'it was the age of wisdom it was the age of foolishness'
wordlist = wordstring.split()
length = len(wordlist)
wordfreq = collections.Counter(wordlist)
Termfrequency = collections.namedtuple('terms','term tf')
tflist = []
for word in wordfreq:
    key = word
    value = wordfreq[key]
    print("{}--{}".format(key,value))
    tflist.append(Termfrequency(term=word,tf=float(value)/length))
print('length is {}'.format(length))
print(tflist)