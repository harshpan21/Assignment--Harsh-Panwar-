morse = { 
    "._": "A", "_..." : "B", "_._.": "C", "_..": "D", ".": "E",
    ".._.": "F", "__.": "G", "....": "H", "..": "I", ".___": "J",
    "_._": "K", "._..": "L", "__": "M", "_.": "N", "___": "O", 
    ".__.": "P", "__._": "Q", "._.": "R", "...": "S", "_": "T",
    ".._": "U", "..._": "V", ".__": "W", "_.._": "X", "_.__": "Y",
    "__..": "Z"

}

code_to_char = {k: v for k, v in morse.items()}

def decode(s, index, path, results):
    if index == len(s):
        results.append("".join(path))
        return
    
    for length in range(1, 5):
        if index + length <= len(s):
            part = s[index:index + length]
            if part in code_to_char:
                path.append(code_to_char[part])
                decode(s, index + length, path, results)
                path.pop()

#word = input("Enter your word:").strip().upper()
encrypted = input().strip()
results = []
decode(encrypted, 0, [], results)


for word in sorted(results):
    print(word)
