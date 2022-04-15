n = input('Enter word\n')
lis= []
li = []
с = 3
def tonum(a):
  l = ord(a)
  return chr(l+с)

def tochr(a):
  l = ord(a)
  return chr(l-с)

print (' Bef - ', n)
for i in n:
  lis.append(tonum(i))

for i in lis:
  li.append(tochr(i))
print(lis)
print(li)