flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]

print(flintstones)
flintstones = flintstones + ["Dino", "Hoppy"]
print(flintstones)

# better solution
flintstones.extend(["Dino", "Hoppy"]) # same behaviour as above