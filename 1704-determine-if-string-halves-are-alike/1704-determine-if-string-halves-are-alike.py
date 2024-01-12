class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s_length = len(s) // 2
        a = s[:s_length].lower()
        b = s[s_length:].lower()
        
        a_vowels = {'a': 0, 'e': 0, 'i':0, 'o':0, 'u':0}
        b_vowels = {'a': 0, 'e': 0, 'i':0, 'o':0, 'u':0}
        
        for char in a:
            if char in a_vowels:
                a_vowels[char] += 1
                
        for char in b:   
            if char in b_vowels:
                b_vowels[char] += 1
                
        return sum(a_vowels.values()) == sum(b_vowels.values())
        
        