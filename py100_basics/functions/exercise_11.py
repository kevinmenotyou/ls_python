def extract_language(locale):
    return locale.split("_")[0]

def extract_region(locale):
    return locale.split(".")[0].split("_")[1]

def local_greet_english(region) -> str:
    match region:
        case "US":
            return "Hey!"
        case "GB":
            return "Hello!"
        case "AU":
            return "Howdy!"
        case _:
            return "Hi!"

def local_greet(locale) -> str:
    language = extract_language(locale)
    region = extract_region(locale)

    match language:
        case 'en':
            return local_greet_english(region)
        case 'fr':
            return "Salut!"
        case 'pt':
            return "Olá!"
        case 'de':
            return "Hallo!"
        case 'sv':
            return "Hej!"
        case 'af':
            return "Haai!"
        case _:
            return "Get out of here!"

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!