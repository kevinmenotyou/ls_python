famous_words = "seven years ago..."
new_string = "Four score and "

print(famous_words)
#famous_words = new_string + famous_words

famous_words = str.join("", [new_string, famous_words])
print(famous_words)

# String interpolation
new_string = f"Four score and {famous_words}"