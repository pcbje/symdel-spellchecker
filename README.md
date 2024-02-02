# Spellchecker with symmetric deletion

This is an illustration of how symmetric deletion can be used to implement a simple spellchecker. It is based on [Norvigs spellchecker](https://norvig.com/spell-correct.html). It shows how inserts, edits, deletions and transpositions in Levenshtein-Damerau distance can be simulated using only deletes. 

Note that this implementation does not produce identical results to the original, as it doesn't find all cases where distance = 2, and sometimes selects a match where distance is 2 but a match with distance 1 exists.

Link to [big.txt](https://norvig.com/big.txt).

## Examples

### Insert
```
$ python3 spell.py answwer
answer
```

### Edit
```
$ python3 spell.py anzwer
answer
```

### Delete
```
$ python3 spell.py anwer 
answer
```

### Transposition
```
$ python3 spell.py ansewr 
answer
```
