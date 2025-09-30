import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold: text = text.casefold()
    if yo2e: text = text.replace('ё', 'е').replace('Ё', 'е')
    text = re.sub(r"\s+", " ", text) # r"\s+" is a regexp for all special characters like \n, \t etc.
    text = text.strip()
    return text

def tokenize(text: str) -> list[str]:
    regexp = r"[^\w-]" # r"[^\w-]" is a regexp for all characters except for letters, numbers and '-'
    text = normalize(re.sub(regexp, " ", text))
    return text.split(' ')

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = dict()
    for token in tokens:
        try: 
            freq[token] += 1
        except:
            freq[token] = 1
    return dict(sorted(freq.items()))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    temp = []
    freq = dict(sorted(freq.items()))
    cnt = 0
    for token in freq.items():
        temp.append(token)
        cnt += 1
        if (cnt == n): break
    return temp
