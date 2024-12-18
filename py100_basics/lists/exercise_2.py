def last (lst):
    if (lst):
        return lst[len(lst)-1]
    else:
        return None

print(last(['Earth', 'Moon', 'Mars']))  # Mars