def scramble(s1, s2):
    from collections import Counter
    return len(Counter(s2)-Counter(s1)) == 0
