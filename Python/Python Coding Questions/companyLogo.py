from collections import Counter

s = input()
print(*[f"{a} {b}" for a, b in Counter(sorted(s)).most_common(3)], sep = "\n")