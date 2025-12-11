import re

def normalize(text: str) -> str:
    text = text.lower()
    text = text.replace('ё', 'е')
    text = re.sub(r'[\r\n\t]', ' ', text)
    text = re.sub(r' +', ' ', text)
    text = text.strip()
    return text

def tokenize(text: str) -> list[str]:
    if not text.strip():
        return []
    return text.split()

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = dict()
    for token in tokens:
        try: 
            freq[token] += 1
        except:
            freq[token] = 1
    return dict(sorted(freq.items(), key=lambda item: (-item[1], item[0])))

def top_n(freq: dict[str, int], n: int) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]

def summarize(string: str, n: int) -> None:
    tokenized = tokenize(string)
    unique_words = count_freq(tokenized)
    print(f"Всего слов: {len(tokenized)}")
    print(f"Уникальных слов: {len(unique_words)}")
    print(f"Топ-{n}:")
    k = top_n(unique_words, n)
    for token in k:
        print("\t"+token[0] + ":" + str(token[1]))
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