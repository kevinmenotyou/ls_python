def starts_with(full_word: str, prefix: str):
    return full_word.find(prefix) == 0

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True