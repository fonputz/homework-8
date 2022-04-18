n = input('Enter word\n')
lis= []
li = []
cypher= 5
def tocypher(a):
  if a ==' ':
    return ' '
  else:
    #УЗНАТИ ЧИСЛО ПО АБЕТЦІ
    index_l = ord(a)-ord('a') 
    #число по абетці + індекс шифрування %(ділим на остаток) 26 = 
    index_c = (index_l+cypher)%26
    #закодувати в унікод число букви
    new_chr = index_c+ord('a')
    return chr(new_chr)

def fromcypher(a):
  if a == ' ':
    return ' '
  else:
    index_l = ord(a)-ord('a') 
    index_c = (index_l-cypher)%26
    new_chr = index_c+ord('a')
    return chr(new_chr)

  

for i in n:
  lis.append(tocypher(i))

for i in lis:
  li.append(fromcypher(i))
print(lis)
print(li)
