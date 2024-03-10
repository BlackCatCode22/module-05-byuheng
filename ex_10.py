fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

many = dict()

for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()

    for w in wds:

        many[w] = many.get(w,0) + 1

# Find the top 5 word by frequency
tmp = dict()
newlist = list()
for k,v in many.items() :
    tup = (v,k)
    newlist.append(tup)

cool = sorted(newlist, reverse=True)

for v,k in cool[:5] :
    print(k,v)