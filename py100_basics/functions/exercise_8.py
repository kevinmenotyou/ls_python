def greet(code: str) -> str:
    match code:
        case 'en':
            return "Hi!"
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

print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!
print(greet('de'))         # Hallo!
print(greet('sv'))         # Hej!
print(greet('af'))         # Haai!
print(greet('ugh'))