# It's a beautiful day! if weather's value is 'sunny'
# Grab your umbrella. if weather's value is 'rainy'
# Let's stay inside. if weather's value is anything else

weather = "snowy"

match weather:
    case "sunny":
        print("It's a beautiful day!")
    case "rainy":
        print ("Grab your umbrella.")
    case _:
        print ("Let's stay inside.")