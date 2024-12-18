destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(name: str, destinations: list):
    try:
        destinations.remove(name)
        return True
    except:
        return False

contains('Barcelona', destinations)  # True
contains('Nashville', destinations)  # False

