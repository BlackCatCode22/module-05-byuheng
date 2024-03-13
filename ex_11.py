# parsing example
data = 'From stephen.marquard@uct.ac.za.Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ',atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)

# double split pattern
words = data.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])

# regex version
import re
#lin = 'From stephen.marquard@uct.ac.za.Sat Jan 5 09:14:16 2008'
y = re.findall('@([^ ]*)',data)
#y = re.findall('^From .@([^ ]*)',data)

print(y)

# spam confidence
import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line in line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.+])', line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))

# escape character
import re
x = 'We just received $10.00 for cookies.'
z = re.findall('\$[0-9.]+',x)
print(z)


