from collections import Counter, defaultdict
from functools import reduce
import re

def words(text): return re.findall(r'\w+', text.lower())

def deletes(word):
    "All permutations that are one permutation away from `word`."
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    return [L + R[1:] for L, R in splits if R]

WORDS = Counter(words(open('big.txt').read()))

"Generate permutations for all `words`"
PERMS = reduce(lambda map, w: [map[P].append(w) for P in [w] + deletes(w)] and False or map, 
               WORDS, defaultdict(list))

def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    return WORDS[word] / N

def correction(word): 
    "Most probable spelling correction for word."    
    return max(candidates(word), key=P)

def candidates(word): 
    "Generate possible spelling corrections for word."
    return known([word]) or known(deletes(word)) or [word]

def known(words): 
    "The subset of `words` that appear in the dictionary of PERMS."    
    return reduce(list.__add__, [PERMS[w] for w in words], [])
