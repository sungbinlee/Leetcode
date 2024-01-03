from collections import Counter
import re 


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        
        counts = (Counter(word))
        return counts.most_common(1)[0][0]