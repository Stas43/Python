def symbolCounterTheBest(s: str):
    symbols = {}
    for char in s:
        symbols[char] = symbols.get(char, 0) + 1
    print(symbols)
    # for char, counter in symbols.items():
    #     print(char, counter)


symbolCounter('aaabbbcccdddddd')
print('\n')
symbolCounterBetter('aaabbbcccdddddd')
print('\n')
symbolCounterTheBest('aaabbbcccdddddd')
