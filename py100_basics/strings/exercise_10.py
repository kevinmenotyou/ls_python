def count_substrings(full_string: str, substring: str):
    count = 0
    while (full_string.find(substring) >= 0):
        index = full_string.find(substring)
        full_string = full_string[index+len(substring):len(full_string)]
        count += 1
    return count

print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0

# def count_substrings(string, substring):
#     return string.count(substring)