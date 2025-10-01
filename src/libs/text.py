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
    return dict(sorted(freq.items(), key=lambda item: (-item[1], item[0])))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    temp = []
    cnt = 0
    for token in freq.items():
        temp.append(token)
        cnt += 1
        if (cnt == n or cnt == len(freq)): break
    return temp

def summarize(string: str) -> None:
    tokenized = tokenize(string)
    unique_words = count_freq(tokenized)
    print(f"Всего слов: {len(tokenized)}")
    print(f"Уникальных слов: {len(unique_words)}")
    n = 5
    print(f"Топ-{n}:")
    k = top_n(unique_words)
    for token in k:
        print(token[0] + ":" + str(token[1]))
    return None

'''print("normalize")
print(f"'ПрИвЕт\nМИр\t' --> {normalize("ПрИвЕт\nМИр\t")}")
print(f"'ёжик, Ёлка' --> {normalize("ёжик, Ёлка")}")
print(f"'Hello\r\nWorld' --> {normalize("Hello\r\nWorld")}")
print(f"'  двойные   пробелы  ' --> {normalize("  двойные   пробелы  ")}")
print("\ntokenize")
print(f"'привет мир' --> {tokenize("привет мир")}")
print(f"'hello,world!!!' --> {tokenize("hello,world!!!")}")
print(f"'по-настоящему круто' --> {tokenize("по-настоящему круто")}")
print(f"'2025 год' --> {tokenize("2025 год" )}")
print(f"'emoji 😀 не слово' --> {tokenize("emoji 😀 не слово")}")

print("\ncount_freq+top_n")
print(f"['a','b','a','c','b','a'] --> {count_freq(["a","b","a","c","b","a"])}; {top_n(count_freq(["a","b","a","c","b","a"]), n=2)}")
print(f"['b','aa','bb','aa','cc'] --> {count_freq(["bb","aa","bb","aa","cc"])}; {top_n(count_freq(["bb","aa","bb","aa","cc"]), n=2)}")
'''