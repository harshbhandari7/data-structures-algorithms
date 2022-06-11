class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        leng = len(password)
        if leng < 8:
            return False
        
        valid_hash = { 'l': False, 'u': False, 'd': False, 's': False, 'r': False}
        
        special_chars = '!@#$%^&*()-+'
        for char in password:
            if char.islower():
                valid_hash['l'] = True
            if char.isupper():
                valid_hash['u'] = True
            if char.isdigit():
                valid_hash['d'] = True
            if char in special_chars:
                valid_hash['s'] = True
                
        for i in range(1, leng):
            if password[i-1] == password[i]:
                valid_hash['r'] = True

        if (valid_hash['l'] and valid_hash['u'] and valid_hash['d'] and valid_hash['s'] and (not valid_hash['r'])):
            return True
        else:
            return False