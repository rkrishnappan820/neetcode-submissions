from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    count_freq = {}
    for char in word:
        if char not in count_freq:
            count_freq[char] = 1
        else:
            count_freq[char] += 1
    return count_freq




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
