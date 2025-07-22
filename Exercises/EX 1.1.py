def double_letters (s):
    for i in range (len(s) - 1):
        if s[i] == s[i+1]:
            return False
    return True
        
print(double_letters('Nts')) 
print(double_letters('muhammad')) 
print(double_letters('socials')) 
print(double_letters('mehbooobs')) 