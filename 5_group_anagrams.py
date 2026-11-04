from collections import defaultdict 

d = defaultdict(list)

def group_anagrams(words):
    for word in words:
        sorted_word = ''.join(sorted(word))
        d[sorted_word].append(word)
    return list(d.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))