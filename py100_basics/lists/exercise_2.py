def last (lst):
    if (lst):
        return lst[len(lst)-1]
        #return lst[-1] python supports negative indexing
    else:
        return None

print(last(['Earth', 'Moon', 'Mars']))  # Mars