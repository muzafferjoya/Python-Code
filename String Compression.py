from collections import Counter
def compress(string):
   s=''
   count=Counter(string)
   for letter in count:
       s+=letter+str(count[letter])
   return s
