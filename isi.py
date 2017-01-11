def is_isogram(string):
  for x in range (0,len(string)-1):
        if string[x:x+1].upper() in string[x+1:len(string)].upper():
            return False
            break
  return True
  
  
print is_isogram('Nython')
