n = input('Enter word\n')
lis= ''
li = ''
abetka = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']
abetka_L = ['А', 'Б', 'В', 'Г', 'Ґ', 'Д', 'Е', 'Є', 'Ж', 'З', 'И', 'І', 'Ї', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ю', 'Я']

#Як прописати функцію ????
def ord_ua(a):
  pass
cypher= 5
def tocypher(a):
  if a ==' ':
    return ' '
  else:
    if a.isupper():
      #УЗНАТИ ЧИСЛО ПО АБЕТЦІ
      index_l = ord(a)-ord('A') 
      #число по абетці + індекс шифрування %(ділим на остаток) 26 = 
      index_c = (index_l+cypher)%26
      #закодувати в унікод число букви 
      new_chr = index_c+ord('A')
      return chr(new_chr)
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
    if a.isupper():
      index_l = ord(a)-ord('A') 
      index_c = (index_l-cypher)%26
      new_chr = index_c+ord('A')
      return chr(new_chr)
    else:
      index_l = ord(a)-ord('a') 
      index_c = (index_l-cypher)%26
      new_chr = index_c+ord('a')
      return chr(new_chr)

  

for i in n:
  lis = lis+tocypher(i)

for i in lis:
  li = li + fromcypher(i)
print(lis)
print(li)
