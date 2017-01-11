

def is_isogram(string):
    #your code here
    for x in range (0,len(string)-1):
        a = string.count(string[x], x, len(string)) 
        if a!=0:
            return False
            break
    return True            
    

print is_isogram('Nython')


